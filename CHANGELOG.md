# Changelog

## Unreleased

### Changed

- Unified public documentation around DoctrineOS as the main project and Doctrine Protocol as the control substrate.
- Renamed the public repository from `doctrine-protocol` to `DoctrineOS`.
- Relicensed project metadata from Apache 2.0 to AGPLv3-or-later.

### Added

- DoctrineOS direction and architecture docs.
- DoctrineOS prototype shell.
- Default DoctrineOS profile.
- Action receipts and runtime state logging.
- Tests for DoctrineOS boot, profile loading, permission refusal, approved action execution, receipt creation, and state creation.

## v0.1.0-prototype

First public DoctrineOS prototype milestone.

### Added

- Public standard doctrine template
- Python SDK
- CLI commands for mount, validate, inspect, and registry build
- Parser and validator
- Mount receipts with context hashes
- Public specification
- Compatibility guidance
- Starter node library
- Generated node registry
- Tests and GitHub Actions validation
- Adapter examples
- DoctrineOS prototype shell
- AGPLv3-or-later licensing

### Public starter nodes

- anti-drift
- clarity
- concise-response
- example
- safety-boundary
- user-authority

### Compatibility floor

A project may be `.doctrine compatible` when it can load doctrine files or concept nodes, parse metadata and sections, validate required structure, produce mounted instruction context, preserve stable IDs and source paths, and keep mount receipts inspectable.
