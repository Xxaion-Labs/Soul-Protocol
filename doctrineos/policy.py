from typing import Dict

from .capability_kernel import MODE_ASK, MODE_OFF


DEFAULT_POLICY_MODES: Dict[str, str] = {
    "network.access": MODE_OFF,
    "shell.run": MODE_ASK,
    "files.read": MODE_ASK,
    "files.write": MODE_ASK,
    "repo.read": MODE_ASK,
    "repo.write": MODE_ASK,
    "model.invoke": MODE_ASK,
    "system.inspect": MODE_ASK,
}
