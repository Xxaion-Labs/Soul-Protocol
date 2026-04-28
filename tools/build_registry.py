import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from doctrine import Doctrine
from tools.node_files import iter_node_paths


def main():
    nodes_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "nodes"
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "registry" / "index.json"

    nodes = []
    for path in iter_node_paths(nodes_dir):
        doctrine = Doctrine.load(path)
        errors = doctrine.validate()
        nodes.append({
            "name": doctrine.name,
            "id": doctrine.id,
            "path": str(path.relative_to(ROOT)) if path.is_absolute() else str(path),
            "definition": doctrine.definition,
            "valid": not bool(errors),
            "errors": errors,
        })

    output = {"nodes": nodes}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps({"written": str(output_path), "count": len(nodes)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
