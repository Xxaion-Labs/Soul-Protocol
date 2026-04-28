# Contributing

Thanks for helping improve Doctrine Protocol. Keep contributions small, clear, and easy to review.

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

## Good contribution types

- Public doctrine nodes
- SDK fixes
- CLI improvements
- Adapter examples
- Documentation improvements
- Tests and validation tooling
- Issue triage

## Pull request rules

- One logical change per PR.
- Include a short summary and testing notes.
- Do not include secrets, API keys, private prompts, private doctrine files, or personal data.
- Keep public nodes generic and reusable.
- Preserve user authority, non-autonomy, non-sentience, safety, clarity, and anti-drift principles.

## Security and privacy

Never include private data in issues, pull requests, examples, tests, or fixtures.

If you find a security concern, open a minimal issue with no sensitive details and mark it clearly as security-related.

## License

By contributing, you agree that your contribution is provided under the repository license.