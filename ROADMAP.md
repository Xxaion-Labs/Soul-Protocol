# Roadmap

Soul Protocol is the public AI-native operating prototype built around `.soul` and Soul Protocol objects.

```text
.soul

    (digital)
A                Soul Protocol object

 ⧉
```

The roadmap moves from public object compatibility to a local userland prototype, then to a broader operating environment.

## Phase 0: Public Soul Object Foundation

Status: active transition.

- public `.soul` standard trajectory
- current `.doctrine` compatibility surface
- SDK and CLI
- parser and validator
- mount receipts with context hashes
- public standard compatibility template
- starter public nodes
- generated node registry
- validation workflow
- AGPLv3-or-later license

## Phase 1: Userland Prototype

Status: complete compatibility prototype.

Goal: prove the control spine before broader system integration.

Complete:

- Soul Protocol compatibility shell
- profile loader
- mount receipt display
- safe command router
- stub adapters
- action log
- permission prompts
- state manifest
- default compatibility profile
- receipt and state tests

The current spine is:

```text
Soul Protocol-compatible object -> mount -> command -> capability -> permission -> adapter -> receipt -> state
```

## Phase 2: Local Runtime

Status: active.

Goal: make Soul Protocol useful on a normal machine.

Planned:

- receipt ledger
- filesystem adapter
- project workspace model
- local model adapter
- terminal adapter with permission gates
- config and profile manager
- rollback points

## Phase 3: Bootable Environment

Goal: ship a user-governed operating environment.

Planned:

- open-base image
- Soul Protocol shell as primary interface
- local-first setup wizard
- profile mounting at startup
- system state dashboard

## Phase 4: AI-Native Desktop

Goal: make the whole environment Soul Protocol-aware.

Planned:

- Soul Protocol-aware launcher
- app and workflow registry
- node package manager
- visible receipts
- permission ledger
- user-controlled automation queues

## Phase 5: Deeper System Integration

Goal: move from userland toward deeper system integration.

Planned:

- service supervision
- policy-governed background tasks
- tighter filesystem indexing
- hardware and device capability models
- stronger sandboxing

## Release discipline

Every public release should remain generic, reusable, auditable, user-governed, non-autonomous, AGPLv3-or-later, and bounded against unsupported claims.
