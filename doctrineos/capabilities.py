from .capability_kernel import (
    DEFAULT_CAPABILITIES,
    Capability,
    CapabilityKernel,
    PolicyDecision,
)


CapabilityRequest = Capability

_DEFAULT_KERNEL = CapabilityKernel()


def get_capability(name: str) -> Capability:
    return _DEFAULT_KERNEL.get(name)


__all__ = [
    "Capability",
    "CapabilityRequest",
    "CapabilityKernel",
    "PolicyDecision",
    "DEFAULT_CAPABILITIES",
    "get_capability",
]
