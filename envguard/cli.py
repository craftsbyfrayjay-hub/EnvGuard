import sys
import os


def parse_env(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(404)

    variables = set()
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if (not line) or line.startswith("#"):
                continue
            if "=" in line:
                key = line.split("=", 1)[0]
                variables.add(key)
    return variables

def print_section(title, items):
    print(title)
    if not items:
        print("✓ None")
    else:
        for v in sorted(items):
            print(f"- {v}")
    print()

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print("Usage: envguard compare <fileA> <fileB>")
        sys.exit(0)

    if len(sys.argv) != 4 or sys.argv[1] != "compare":
        print("Usage: envguard compare <fileA> <fileB>")
        sys.exit(0)

    file_a = sys.argv[2]
    file_b = sys.argv[3]

    vars_a = parse_env(file_a)
    vars_b = parse_env(file_b)

    missing = vars_a - vars_b
    extra = vars_b - vars_a

    print_section("Missing:", missing)
    print_section("Extra:", extra)

    exit_code = 0
    if missing and extra:
        exit_code = 3
    elif missing:
        exit_code = 1
    elif extra:
        exit_code = 2

    sys.exit(exit_code)


if __name__ == "__main__":
    main()