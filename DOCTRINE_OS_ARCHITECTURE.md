# DoctrineOS Architecture Seed

DoctrineOS is a whole-system direction, not a single assistant feature.

## Layer Model

```text
DoctrineOS
├─ Base System
│  └─ Linux or another open base capable of booting real hardware
├─ Doctrine Control Layer
│  └─ doctrine mounts, authority policy, receipts, validation, profiles
├─ AI System Shell
│  └─ user-facing command surface for natural language and structured commands
├─ Capability Layer
│  └─ permissioned access to files, shell, apps, network, models, and tools
├─ Adapter Layer
│  └─ model adapters, local tools, APIs, filesystem, browser, editor, repo tools
├─ State Layer
│  └─ manifests, logs, hashes, receipts, rollback points, project context
├─ Node Package Layer
│  └─ installable doctrine nodes and public behavior packages
├─ Application Layer
│  └─ doctrine-aware apps and workflows
└─ User Authority Layer
   └─ the human remains root authority
```

## First Build Target

The first practical target is not a custom kernel.

The first target is a doctrine-native userland running on an open base system:

1. bootable environment later
2. local command shell first
3. doctrine mounting before automation
4. receipts before trust
5. user authority before autonomy

## Operating Principles

- The OS must be user-governed.
- The AI layer must remain non-autonomous.
- Actions must be inspectable.
- Powerful actions must be permissioned.
- State must be legible and recoverable.
- Doctrine must be mountable, composable, and verifiable.
- Public code must remain open under AGPLv3-or-later.

## First Milestone

Create a minimal DoctrineOS shell that can:

- load a doctrine profile
- mount it
- emit a receipt
- accept user commands
- route commands to safe stub adapters
- log actions
- show state
- refuse unpermissioned actions

This proves the OS control spine before attempting a full desktop or kernel-level integration.
