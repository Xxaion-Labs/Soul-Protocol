# Compatibility

DoctrineOS compatibility begins with support for the public `⧉` standard.

`⧉` is the object. In prose, call it **a tesseract**.

The current public compatibility surface is `.doctrine`.

A project is compatible when it can use the public `.doctrine` surface to load, validate, mount, and inspect tesseract material without requiring closed custom extensions.

## Minimum requirements

A compatible tool can:

- load `.doctrine` files or concept nodes
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
⧉ compatible
```

when they support the minimum requirements above.

Projects may also say:

```text
.doctrine compatible
```

when they specifically mean compatibility with the current public `.doctrine` surface.

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
