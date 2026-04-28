# Doctrine Filetype v1

Doctrine files use the `.doctrine` extension and are plain UTF-8 text.

A doctrine file has two readable layers:

- Markdown sections for people and language models.
- Optional JSON sentinel blocks for software tools.

Sentinel block form:

```text
<<<NAME_JSON>>>
{"key":"value"}
<<<END_NAME_JSON>>>
```

A basic compatible tool should read UTF-8 text, parse top metadata, parse `##` sections, parse JSON sentinel blocks when present, render instruction context, and emit an inspectable mount receipt.

Doctrine files should remain standalone. External files can inform a doctrine, but should not be required to read or mount it.
