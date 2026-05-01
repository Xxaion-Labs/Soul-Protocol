# Compatibility

DoctrineOS compatibility begins with support for `.glyph` Tesseracts.

```text
.glyph

    (digital)
A                Tesseract

 ⧉
```

The current implementation also supports the `.doctrine` compatibility surface during transition.

## Minimum requirements

A compatible tool can:

- load `.glyph`, `.doctrine`, or concept node files
- parse metadata and section headings
- parse JSON sentinel blocks when present
- report sentinel parse errors instead of silently ignoring them
- validate required node structure
- produce mounted instruction context
- preserve stable IDs and source paths when available
- keep mount receipts inspectable

## Badge language

Projects may say:

```text
.glyph compatible
```

when they support the forward public filetype surface.

Projects may say:

```text
.doctrine compatible
```

when they specifically support the current compatibility surface.

## DoctrineOS ecosystem fit

Compatible projects can act as:

- model adapters
- editor integrations
- local scripts
- services
- workflow runners
- node registries
- OS-level components

The compatibility floor stays intentionally simple so builders can fork, inspect, implement, and improve it.

## Boundary

Compatibility does not imply AI sentience, autonomy, independent will, physical four-dimensional geometry, or unsupported capability claims.
