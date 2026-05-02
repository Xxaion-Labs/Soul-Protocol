# Compatibility

Compatibility is the public handshake.

A compatible tool does not need to implement the whole future of Soul Protocol. It only needs to honor the first law of the object: readable meaning can become structured runtime context without hiding authority from the user.

## Compatibility target

Soul Protocol compatibility begins with support for `.soul` objects.

The current implementation also supports the `.doctrine` compatibility surface during transition.

```text
.soul object or compatibility file
  -> parse
  -> validate
  -> mount
  -> receipt
  -> instruction context
```

## Minimum requirements

A compatible tool can:

- load `.soul`, `.doctrine`, or concept node files
- parse metadata and section headings
- parse JSON sentinel blocks when present
- report sentinel parse errors instead of silently ignoring them
- validate required node structure
- produce mounted instruction context
- preserve stable IDs and source paths when available
- keep mount receipts inspectable

## Badge language

Projects may say `.soul compatible` when they support the forward public filetype trajectory.

Projects may say `.doctrine compatible` when they specifically support the current compatibility surface.

## Ecosystem fit

Compatible projects can become:

- model adapters
- editor integrations
- local scripts
- services
- workflow runners
- node registries
- system components
- profile managers
- receipt viewers
- permission dashboards

The compatibility floor is intentionally small. It is meant to be copied, forked, audited, implemented, and improved.

## Compatibility principle

A compatible implementation should preserve the chain:

```text
source -> structure -> mount -> receipt -> context -> capability -> permission
```

If a tool breaks that chain, it may still be useful, but it is no longer carrying the full public shape of Soul Protocol.

## Boundary

Compatibility does not imply unsupported capability claims. Implementations should keep authority, permission, receipts, and user control explicit.
