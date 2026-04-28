# Doctrine Native Filetype v1

This document defines the public native-filetype floor for `.doctrine` files.

## Identity

- Extension: `.doctrine`
- Preferred MIME: `text/x-doctrine`
- Fallback MIME: `text/plain`
- Windows ProgID: `XxaionLabs.Doctrine.1`
- macOS UTI: `com.xxaionlabs.doctrine`
- Linux XDG MIME: `text/x-doctrine`

## Layers

A `.doctrine` file is plain UTF-8 text with:

1. Markdown semantic sections.
2. Optional JSON sentinel blocks.
3. A compiled doctrine state emitted by a parser or runtime.
4. Inspectable mount and validation receipts.

## Native opener

The recommended specialized opener is Doctrine Workbench.

A Doctrine Workbench should show:

- structure tree and sentinel index
- Markdown doctrine law
- JSON sentinel layer
- compiled doctrine state
- mount receipt and validation errors
- hash, certificate, and dependency-sovereignty diagnostics

The raw `.doctrine` file remains the source of truth. A workbench is only a projection.

## Parser chain

A compatible parser should run:

```text
BYTE_READ -> DECODE_UTF8 -> PARSE_METADATA -> PARSE_SECTIONS -> PARSE_JSON_SENTINELS -> EMIT_COMPILED_STATE -> EMIT_MOUNT_RECEIPT
```

## Round trip

Opening a `.doctrine` file should not silently rewrite it. Saving should preserve UTF-8. Formatting, canonicalization, and certificate restamping should be explicit.
