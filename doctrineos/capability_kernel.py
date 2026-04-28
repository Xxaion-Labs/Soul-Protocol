from dataclasses import dataclass, replace
from typing import Dict, Mapping, Optional


MODE_OFF = "off"
MODE_ASK = "ask"
MODE_ALLOW = "allow"

RISK_LOW = "low"
RISK_MEDIUM = "medium"
RISK_HIGH = "high"
RISK_CRITICAL = "critical"


@dataclass(frozen=True)
class Capability:
    name: str
    description: str
    risk_level: str
    default_mode: str
    requires_receipt: bool
    adapter_binding: str

    @property
    def requires_permission(self) -> bool:
        return self.default_mode == MODE_ASK


@dataclass(frozen=True)
class PolicyDecision:
    capability: Capability
    mode: str
    allowed: bool
    requires_permission: bool
    requires_receipt: bool
    reason: str


DEFAULT_CAPABILITIES: Dict[str, Capability] = {
    "none": Capability(
        name="none",
        description="No external capability required.",
        risk_level=RISK_LOW,
        default_mode=MODE_ALLOW,
        requires_receipt=True,
        adapter_binding="runtime.none",
    ),
    "state.read": Capability(
        name="state.read",
        description="Read DoctrineOS runtime state.",
        risk_level=RISK_LOW,
        default_mode=MODE_ALLOW,
        requires_receipt=True,
        adapter_binding="state.read",
    ),
    "system.inspect": Capability(
        name="system.inspect",
        description="Inspect local system or runtime metadata.",
        risk_level=RISK_LOW,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="system.inspect",
    ),
    "files.read": Capability(
        name="files.read",
        description="Read workspace files or directories.",
        risk_level=RISK_MEDIUM,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="filesystem.read",
    ),
    "files.write": Capability(
        name="files.write",
        description="Write workspace files.",
        risk_level=RISK_HIGH,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="filesystem.write",
    ),
    "repo.read": Capability(
        name="repo.read",
        description="Read repository status, history, or diffs.",
        risk_level=RISK_MEDIUM,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="repo.read",
    ),
    "repo.write": Capability(
        name="repo.write",
        description="Change repository contents or refs.",
        risk_level=RISK_HIGH,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="repo.write",
    ),
    "shell.run": Capability(
        name="shell.run",
        description="Run a shell command.",
        risk_level=RISK_HIGH,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="shell.run",
    ),
    "network.access": Capability(
        name="network.access",
        description="Access network resources.",
        risk_level=RISK_HIGH,
        default_mode=MODE_OFF,
        requires_receipt=True,
        adapter_binding="network.access",
    ),
    "model.invoke": Capability(
        name="model.invoke",
        description="Invoke a local or remote model adapter.",
        risk_level=RISK_MEDIUM,
        default_mode=MODE_ASK,
        requires_receipt=True,
        adapter_binding="model.invoke",
    ),
}


class CapabilityKernel:
    def __init__(
        self,
        capabilities: Optional[Mapping[str, Capability]] = None,
        policy_modes: Optional[Mapping[str, str]] = None,
    ):
        self.capabilities: Dict[str, Capability] = dict(capabilities or DEFAULT_CAPABILITIES)
        self.policy_modes: Dict[str, str] = dict(policy_modes or {})

    def get(self, name: str) -> Capability:
        capability = self.capabilities.get(name)
        if capability is not None:
            return self._apply_policy(capability)
        return Capability(
            name=name,
            description="Unknown capability.",
            risk_level=RISK_HIGH,
            default_mode=MODE_ASK,
            requires_receipt=True,
            adapter_binding="unknown",
        )

    def evaluate(self, name: str, approved: Optional[bool] = None) -> PolicyDecision:
        capability = self.get(name)
        mode = capability.default_mode

        if mode == MODE_OFF:
            return PolicyDecision(
                capability=capability,
                mode=mode,
                allowed=False,
                requires_permission=False,
                requires_receipt=capability.requires_receipt,
                reason="blocked by policy",
            )

        if mode == MODE_ALLOW:
            return PolicyDecision(
                capability=capability,
                mode=mode,
                allowed=True,
                requires_permission=False,
                requires_receipt=capability.requires_receipt,
                reason="allowed by policy",
            )

        if mode == MODE_ASK:
            allowed = bool(approved)
            return PolicyDecision(
                capability=capability,
                mode=mode,
                allowed=allowed,
                requires_permission=True,
                requires_receipt=capability.requires_receipt,
                reason="approved by user" if allowed else "permission required",
            )

        return PolicyDecision(
            capability=capability,
            mode=mode,
            allowed=False,
            requires_permission=True,
            requires_receipt=capability.requires_receipt,
            reason="invalid policy mode",
        )

    def describe(self) -> Dict[str, Dict[str, str]]:
        described: Dict[str, Dict[str, str]] = {}
        for name in sorted(self.capabilities):
            capability = self.get(name)
            described[name] = {
                "description": capability.description,
                "risk_level": capability.risk_level,
                "mode": capability.default_mode,
                "adapter_binding": capability.adapter_binding,
            }
        return described

    def _apply_policy(self, capability: Capability) -> Capability:
        override = self.policy_modes.get(capability.name)
        if override is None:
            return capability
        return replace(capability, default_mode=override)
