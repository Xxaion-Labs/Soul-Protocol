# Contributing

Thanks for helping improve Soul Protocol.

This project is building public control matter for AI-native systems. Contributions should keep that spirit: clear enough to inspect, small enough to review, and disciplined enough to preserve user authority.

## Start here

1. Fork the repository.
2. Create a focused branch:

```bash
git checkout -b feat/short-description
```

3. Open pull requests against `main` unless a maintainer asks for a different target.

## Development

```bash
pip install -e . pytest
python -m pytest
python tools/validate_nodes.py
python tools/check_registry.py
```

When adding or changing public nodes, update the registry:

```bash
python tools/build_registry.py
python tools/check_registry.py
```

## What good contributions preserve

A good contribution strengthens the chain:

```text
readable source -> structured mount -> receipt -> capability boundary -> permission -> recoverable state
```

The code should feel mundane where it touches machines and profound where it reveals the shape. Prefer inspectable mechanisms over clever opacity.

## Good contribution types

- Soul Protocol runtime improvements
- SDK fixes
- CLI improvements
- public nodes
- adapter examples
- documentation improvements
- tests and validation tooling
- issue triage
- receipt and state inspection improvements
- capability and permission hardening

## Pull request rules

- One logical change per PR.
- Include a short summary and testing notes.
- Do not include sensitive, non-public, credentialed, or personal material.
- Keep public nodes generic and reusable.
- Preserve user authority, safety, clarity, and anti-drift principles.
- Keep behavior inspectable.
- Add tests when a change affects parsing, mounting, validation, receipts, capabilities, or state.

## Security and privacy

Never include sensitive or non-public data in issues, pull requests, examples, tests, or fixtures.

If you find a security concern, open a minimal issue with no sensitive details and mark it clearly as security-related.

## License

By contributing, you agree that your contribution is provided under the repository license.
