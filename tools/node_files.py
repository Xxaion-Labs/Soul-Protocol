from pathlib import Path

NODE_FILE_EXCLUDES = {"README.md"}


def iter_node_paths(nodes_dir):
    nodes_dir = Path(nodes_dir)
    return sorted(
        path
        for path in nodes_dir.glob("*.md")
        if path.name not in NODE_FILE_EXCLUDES and not path.name.startswith("_")
    )
