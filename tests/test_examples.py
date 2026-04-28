from pathlib import Path

from examples.api_payload_adapter import build_payload
from examples.local_model_prompt import build_local_prompt
from examples.prompt_context_export import export_context


def test_api_payload_adapter():
    payload = build_payload("hello")
    assert "system" in payload
    assert payload["user"] == "hello"
    assert payload["metadata"]["doctrine_id"] == "standard_public_doctrine_body_v1"
    assert payload["metadata"]["context_sha256"]


def test_local_model_prompt():
    prompt = build_local_prompt("hello")
    assert "# Doctrine: standard_public_doctrine_body_v1" in prompt
    assert "User:" in prompt
    assert "hello" in prompt


def test_prompt_context_export(tmp_path):
    output_path = tmp_path / "mounted_context.txt"
    returned = export_context(output_path)
    assert Path(returned).exists()
    text = output_path.read_text(encoding="utf-8")
    assert "# Doctrine: standard_public_doctrine_body_v1" in text
