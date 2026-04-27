"""Public .doctrine SDK.

This module implements the public protocol surface:
load -> parse -> validate -> mount -> inspect/export.
It intentionally contains only generic public mount behavior.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
import hashlib
import json
import re

REQUIRED_NODE_SECTIONS = ("Definition", "Usage", "Example", "ID")


class DoctrineError(Exception):
    """Base error for Doctrine SDK failures."""


class DoctrineValidationError(DoctrineError):
    """Raised when a doctrine document is structurally invalid."""


@dataclass
class DoctrineSection:
    title: str
    body: str

    def to_dict(self) -> Dict[str, str]:
        return {"title": self.title, "body": self.body}


@dataclass
class DoctrineMount:
    doctrine_id: str
    name: str
    source: Optional[str]
    sections: List[DoctrineSection]
    metadata: Dict[str, str] = field(default_factory=dict)

    def to_context(self) -> Dict[str, Any]:
        return {
            "mounted": True,
            "id": self.doctrine_id,
            "name": self.name,
            "source": self.source,
            "metadata": self.metadata,
            "sections": [section.to_dict() for section in self.sections],
            "instruction_context": self.render_instruction_context(),
        }

    def render_instruction_context(self) -> str:
        lines = [f"# Mounted Doctrine: {self.name}", f"ID: {self.doctrine_id}"]
        for section in self.sections:
            lines.append(f"\n## {section.title}\n{section.body}".strip())
        return "\n\n".join(lines).strip()

    def receipt(self) -> Dict[str, Any]:
        payload = self.to_context()
        rendered = payload["instruction_context"]
        payload["receipt_sha256"] = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
        return payload


@dataclass
class Doctrine:
    name: str
    definition: Optional[str] = None
    id: Optional[str] = None
    usage: Optional[str] = None
    example: Optional[str] = None
    sections: List[DoctrineSection] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
    source: Optional[str] = None

    @classmethod
    def load(cls, path: str | Path) -> "Doctrine":
        source = Path(path)
        text = source.read_text(encoding="utf-8-sig")
        doctrine = cls.from_text(text, source=str(source))
        return doctrine

    @classmethod
    def from_text(cls, text: str, source: Optional[str] = None) -> "Doctrine":
        metadata = _parse_metadata(text)
        sections = _parse_sections(text)
        name = _parse_name(text, source)
        definition = _section_body(sections, "Definition")
        usage = _section_body(sections, "Usage")
        example = _section_body(sections, "Example")
        doctrine_id = _section_body(sections, "ID") or metadata.get("body_id") or _short_hash(text)
        return cls(
            name=name,
            definition=definition,
            id=doctrine_id,
            usage=usage,
            example=example,
            sections=sections,
            metadata=metadata,
            source=source,
        )

    def validate(self, require_node_sections: bool = False) -> List[str]:
        errors: List[str] = []
        if not self.name:
            errors.append("missing name")
        if not self.id:
            errors.append("missing id")
        if require_node_sections:
            titles = {section.title for section in self.sections}
            for required in REQUIRED_NODE_SECTIONS:
                if required not in titles:
                    errors.append(f"missing section: {required}")
        if errors:
            raise DoctrineValidationError("; ".join(errors))
        return []

    def mount(self, validate: bool = True) -> Dict[str, Any]:
        if validate:
            self.validate(require_node_sections=False)
        mount = DoctrineMount(
            doctrine_id=self.id or _short_hash(self.name),
            name=self.name,
            source=self.source,
            sections=self.sections,
            metadata=self.metadata,
        )
        return mount.to_context()

    def receipt(self) -> Dict[str, Any]:
        mount = DoctrineMount(
            doctrine_id=self.id or _short_hash(self.name),
            name=self.name,
            source=self.source,
            sections=self.sections,
            metadata=self.metadata,
        )
        return mount.receipt()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "id": self.id,
            "definition": self.definition,
            "usage": self.usage,
            "example": self.example,
            "source": self.source,
            "metadata": self.metadata,
            "sections": [section.to_dict() for section in self.sections],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


def compose(doctrines: Iterable[Doctrine]) -> Dict[str, Any]:
    mounted = [doctrine.mount() for doctrine in doctrines]
    rendered = "\n\n---\n\n".join(item["instruction_context"] for item in mounted)
    return {
        "mounted": True,
        "count": len(mounted),
        "items": mounted,
        "instruction_context": rendered,
        "receipt_sha256": hashlib.sha256(rendered.encode("utf-8")).hexdigest(),
    }


def _parse_metadata(text: str) -> Dict[str, str]:
    metadata: Dict[str, str] = {}
    for raw in text.splitlines()[:20]:
        line = raw.strip()
        if not line or line.startswith("#") or line == "---":
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key and re.match(r"^[A-Za-z_][A-Za-z0-9_-]*$", key):
                metadata[key] = value
    return metadata


def _parse_sections(text: str) -> List[DoctrineSection]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    sections: List[DoctrineSection] = []
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections.append(DoctrineSection(title=title, body=body))
    return sections


def _parse_name(text: str, source: Optional[str]) -> str:
    node_match = re.search(r"^#\s*Node:\s*(.+?)\s*$", text, re.MULTILINE)
    if node_match:
        return node_match.group(1).strip()
    title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    metadata = _parse_metadata(text)
    if metadata.get("body_id"):
        return metadata["body_id"]
    if source:
        return Path(source).stem
    return "doctrine"


def _section_body(sections: Iterable[DoctrineSection], title: str) -> Optional[str]:
    for section in sections:
        if section.title.lower() == title.lower():
            return section.body.strip()
    return None


def _short_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
