import sys
import argparse
from sql2mermaid import convert

def main():
    parser = argparse.ArgumentParser(description="Convert SQL to Mermaid ERD.")
    parser.add_argument('file', nargs='?', metavar='FILE', help="SQL file to convert (defaults to stdin)")
    args = parser.parse_args()
    try:
        if args.file:
            with open(args.file, 'r') as f:
                query = f.read()
        else:
            query = sys.stdin.read()
        mermaid_output = convert(query)
        print(mermaid_output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
