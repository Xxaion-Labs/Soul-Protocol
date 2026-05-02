# Architecture

Soul Protocol is a user-governed AI-native operating prototype built around mountable Soul Protocol objects.

```text
.soul

    (digital)
A                Soul Protocol object

 ⧉
```

The symbol is the object. In prose, call it **a Soul Protocol object**.

Soul Protocol begins as a userland runtime on an open base system and grows toward an AI-native operating environment: not another app around intelligence, but a control surface where intelligence is mounted through readable objects, bounded by permission, and made accountable through receipts.

## Control spine

The spine is deliberately simple:

```text
Soul Protocol object
  -> mount
  -> instruction context
  -> command
  -> capability check
  -> permission gate
  -> adapter
  -> action receipt
  -> runtime state
```

Each step exists to keep power legible.

- The object stores meaning.
- The mount converts meaning into context.
- The command names the intended action.
- The capability check identifies the power required.
- The permission gate keeps the user in authority.
- The adapter touches the outside world.
- The receipt records what happened.
- The state layer keeps the system recoverable.

## Layer model

```text
Soul Protocol
├─ Base System
│  └─ open host environment capable of running the public runtime
├─ Soul Protocol Control Layer
│  └─ .soul trajectory, .doctrine-compatible mounts, authority policy, receipts, validation, profiles
├─ AI System Shell
│  └─ user-facing command surface for natural language and structured commands
├─ Capability Layer
│  └─ permissioned access to files, shell, apps, network, models, and tools
├─ Adapter Layer
│  └─ model adapters, local tools, APIs, filesystem, browser, editor, repo tools
├─ State Layer
│  └─ manifests, logs, hashes, receipts, rollback points, project context
├─ Node Package Layer
│  └─ installable public behavior nodes and packages
├─ Application Layer
│  └─ Soul Protocol-aware apps and workflows
└─ User Authority Layer
   └─ the human remains root authority
```

## Mounting

Mounting is the act that turns a readable artifact into runtime context.

A mount does not grant autonomy. A mount prepares structured context. The runtime may then use that context to shape outputs, route commands, validate requirements, or constrain adapter behavior.

The mount receipt is the proof surface. It records what was mounted, where it came from, and what context hash resulted.

## Capability and permission

Soul Protocol treats capability as a named boundary.

A runtime should know when an action requires file access, shell access, network access, model access, or another power-bearing operation. Permissioned actions should ask before crossing that boundary.

## Receipts

Receipts are how the system resists fog.

A receipt should make an action inspectable after it happens. It does not prove more than it records, but it gives the user and future tooling a durable trail.

## First build target

The first practical target is not a custom kernel.

The first target is a Soul Protocol-aware userland running on an open base system:

1. local command shell first
2. mounting before automation
3. receipts before trust
4. user authority before autonomy
5. broader operating environment later

## Operating principles

- The system must be user-governed.
- The AI layer must remain non-autonomous.
- Actions must be inspectable.
- Powerful actions must be permissioned.
- State must be legible and recoverable.
- Soul Protocol objects must be mountable, composable, and verifiable.
- Public code must remain open under AGPLv3-or-later.

## Boundary

Soul Protocol does not claim AI sentience, autonomy, independent will, unsupported capability, or physical four-dimensional geometry.
