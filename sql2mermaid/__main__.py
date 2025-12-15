import argparse
import sys

from sql2mermaid import convert


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert SQL to Mermaid ERD.")
    parser.add_argument("file", nargs="?", metavar="FILE", help="SQL file to convert (defaults to stdin)")
    parser.add_argument("--root", type=str, default="root", help="Name of the root table (default: 'root')")
    parser.add_argument(
        "--display-join", choices=["none", "upper", "lower"], default="none", help="Display join type (default: 'none')"
    )
    args = parser.parse_args()
    try:
        if args.file:
            with open(args.file, "r") as f:
                query = f.read()
        else:
            query = sys.stdin.read()
        mermaid_output = convert(query, root_name=args.root, display_join=args.display_join)
        print(mermaid_output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
