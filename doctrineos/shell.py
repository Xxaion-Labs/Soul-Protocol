import argparse
import json
from typing import Optional

from .runtime import DoctrineOSRuntime


def format_boot(status):
    return "\n".join([
        "DoctrineOS",
        "Profile: " + status["profile"],
        "Mount: " + status["mount"],
        "Context: " + status["context_sha256"],
        "User authority: " + status["user_authority"],
        "Capabilities:",
        "  files.read: " + status["capabilities"]["files.read"],
        "  shell.run: " + status["capabilities"]["shell.run"],
        "  network.access: " + status["capabilities"]["network.access"],
        "  model: " + status["capabilities"]["model"],
    ])


def run_once(runtime: DoctrineOSRuntime, command: str, yes: bool = False) -> int:
    plan = runtime.plan(command)
    if plan["requires_permission"] and not yes:
        print("Intent detected: " + str(plan["intent"]))
        print("Capability needed: " + str(plan["capability"]))
        print("Permission required: yes")
        response = input("Proceed? y/n: ").strip().lower()
        approved: Optional[bool] = response in {"y", "yes"}
    else:
        approved = True

    output = runtime.execute(command, approved=approved)
    print(output["result"])
    print("Receipt: " + output["receipt_path"])
    return 0


def interactive(runtime: DoctrineOSRuntime) -> int:
    print(format_boot(runtime.boot_status()))
    while True:
        try:
            command = input("doctrineos> ").strip()
        except EOFError:
            print()
            return 0
        if command in {"exit", "quit", "/bye"}:
            return 0
        if not command:
            continue
        run_once(runtime, command)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="DoctrineOS prototype shell")
    parser.add_argument("command", nargs="*", help="Command to run once. Omit for interactive shell.")
    parser.add_argument("--profile", default="standard_public_template.doctrine", help="Doctrine profile path")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    parser.add_argument("--state-dir", default=".doctrineos", help="State directory")
    parser.add_argument("--json", action="store_true", help="Print boot status as JSON")
    parser.add_argument("--yes", action="store_true", help="Approve permission prompts for this command")
    args = parser.parse_args(argv)

    runtime = DoctrineOSRuntime(
        profile_path=args.profile,
        workspace=args.workspace,
        state_dir=args.state_dir,
    )

    if args.json and not args.command:
        print(json.dumps(runtime.boot_status(), indent=2))
        return 0

    if args.command:
        return run_once(runtime, " ".join(args.command), yes=args.yes)

    return interactive(runtime)


if __name__ == "__main__":
    raise SystemExit(main())
