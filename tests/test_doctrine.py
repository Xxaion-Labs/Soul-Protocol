from doctrine import Doctrine


def test_load_example_node():
    doctrine = Doctrine.load("nodes/example.md")
    assert doctrine.name == "example"
    assert doctrine.id == "example-1"
    assert doctrine.definition == "Minimal reusable concept."


def test_validate_example_node():
    doctrine = Doctrine.load("nodes/example.md")
    assert doctrine.validate() == []


def test_mount_example_node():
    doctrine = Doctrine.load("nodes/example.md")
    mounted = doctrine.mount()
    assert mounted["mounted"] is True
    assert mounted["name"] == "example"
    assert mounted["id"] == "example-1"
    assert "instruction_context" in mounted
    assert "context_sha256" in mounted


def test_load_standard_public_template():
    doctrine = Doctrine.load("standard_public_template.doctrine")
    assert doctrine.name == "standard_public_doctrine_body_v1"
    assert doctrine.id == "standard_public_doctrine_body_v1"
    assert "1. Authority Law" in doctrine.sections


def test_compose_nodes():
    one = Doctrine.load("nodes/example.md")
    two = Doctrine.load("standard_public_template.doctrine")
    composed = Doctrine.compose([one, two], name="composed-test")
    mounted = composed.mount(strict=False)
    assert mounted["mounted"] is True
    assert mounted["name"] == "composed-test"
