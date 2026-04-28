# Capabilities

DoctrineOS uses capabilities to describe what kind of power a command wants to use.

The capability kernel is the first Phase 2 local-runtime layer. It turns simple labels into policy decisions that the runtime can inspect, enforce, receipt, and explain.

## Capability modes

A capability can be in one of three modes:

```text
off    -> blocked by policy
ask    -> requires explicit user approval
allow  -> allowed by policy
```

## Risk levels

Capabilities use public risk labels:

```text
low
medium
high
critical
```

The current kernel uses these labels for inspection and receipts. Later runtime layers can use them for stronger prompts, queues, dashboards, sandboxing, and release policy.

## Current capabilities

```text
none
state.read
system.inspect
files.read
files.write
repo.read
repo.write
shell.run
network.access
model.invoke
```

## Default policy

The default public policy is conservative:

```text
state.read       allow
files.read       ask
files.write      ask
repo.read        ask
repo.write       ask
shell.run        ask
network.access   off
model.invoke     ask
system.inspect   ask
```

## Runtime flow

The current runtime flow is:

```text
command -> plan -> capability -> policy decision -> adapter or refusal -> receipt -> state
```

Every action receives a policy decision with:

- capability
- mode
- allowed/blocked result
- permission requirement
- receipt requirement
- reason

Action receipts include capability policy fields so users can inspect why an action ran or why it was refused.

## Design rule

The capability kernel does not make DoctrineOS autonomous.

It gives the user-governed runtime a clear way to decide whether a command should be allowed, blocked, or sent to the user for approval.
