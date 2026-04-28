# DoctrineOS Prototype Shell

The DoctrineOS prototype shell is the first runnable operating surface for the DoctrineOS direction.

It proves the control spine before any full desktop, distro, or kernel-level integration.

## Run

```bash
doctrineos
```

Print boot status as JSON:

```bash
doctrineos --json
```

Run one command:

```bash
doctrineos inspect workspace
```

Approve a permissioned command for scripts or tests:

```bash
doctrineos --yes inspect workspace
```

## What it proves

The shell can:

- load a doctrine profile
- mount the doctrine profile
- emit mount-aware action receipts
- accept user commands
- plan the command intent
- identify needed capabilities
- ask permission for capability use
- route approved commands to safe stub adapters
- log state
- refuse unapproved permissioned actions

## Current capabilities

- `files.read`: asks before inspecting workspace files
- `shell.run`: modeled as permissioned, not implemented yet
- `network.access`: off by default
- `model`: stub

## State and receipts

By default, runtime state is written under:

```text
.doctrineos/
```

Action receipts are written under:

```text
.doctrineos/receipts/
```

This is an early prototype. It is intentionally small, inspectable, and safe by default.
