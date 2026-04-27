import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from doctrine import Doctrine


def main():
    nodes_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "nodes"
    results = []
    failed = False

    for path in sorted(nodes_dir.glob("*.md")):
        doctrine = Doctrine.load(path)
        errors = doctrine.validate()
        if errors:
            failed = True
        results.append({
            "path": str(path),
            "name": doctrine.name,
            "id": doctrine.id,
            "valid": not bool(errors),
            "errors": errors,
        })

    print(json.dumps({"nodes": results}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
