from doctrineos.runtime import DoctrineOSRuntime
from doctrineos.shell import main


def test_doctrineos_boot_status(tmp_path):
    runtime = DoctrineOSRuntime(state_dir=str(tmp_path / "state"))
    status = runtime.boot_status()
    assert status["system"] == "DoctrineOS"
    assert status["mount"] == "verified"
    assert status["user_authority"] == "root"
    assert status["context_sha256"]


def test_doctrineos_refuses_unapproved_permissioned_action(tmp_path):
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(tmp_path / "state"))
    output = runtime.execute("inspect workspace", approved=False)
    assert output["allowed"] is False
    assert "refused" in output["result"]
    assert output["receipt"]["allowed"] is False


def test_doctrineos_executes_approved_stub_action(tmp_path):
    (tmp_path / "example.txt").write_text("hello", encoding="utf-8")
    runtime = DoctrineOSRuntime(workspace=str(tmp_path), state_dir=str(tmp_path / "state"))
    output = runtime.execute("inspect workspace", approved=True)
    assert output["allowed"] is True
    assert "example.txt" in output["result"]
    assert output["receipt"]["capability"] == "files.read"


def test_doctrineos_cli_json_boot(capsys):
    result = main(["--json"])
    captured = capsys.readouterr()
    assert result == 0
    assert "DoctrineOS" in captured.out
