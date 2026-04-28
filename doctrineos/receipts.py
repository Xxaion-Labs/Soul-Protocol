import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


def stable_hash(payload: Dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_action_receipt(
    command: str,
    intent: str,
    capability: str,
    allowed: bool,
    result: str,
    doctrine_receipt: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    receipt = {
        "type": "doctrineos.action_receipt",
        "timestamp": utc_now(),
        "command": command,
        "intent": intent,
        "capability": capability,
        "allowed": allowed,
        "result": result,
        "doctrine_context_sha256": (doctrine_receipt or {}).get("context_sha256"),
    }
    receipt["receipt_sha256"] = stable_hash(receipt)
    return receipt


def write_receipt(receipt: Dict[str, Any], receipts_dir: Path) -> Path:
    receipts_dir.mkdir(parents=True, exist_ok=True)
    safe_time = receipt["timestamp"].replace(":", "-").replace("+", "Z")
    path = receipts_dir / (safe_time + "-" + receipt["receipt_sha256"][:12] + ".json")
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    return path
