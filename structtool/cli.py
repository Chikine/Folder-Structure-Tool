from pathlib import Path
import sys

APP_DIR = Path.home() / ".structtool"
STRUCTURES_DIR = APP_DIR / "structures"
STRUCTURES_DIR.mkdir(parents=True, exist_ok=True)

def save_structure(struct_name, source_folder):
    source = Path(source_folder)

    if not source.exists():
        print(f"Error: '{source}' does not exist.")
        return 1

    output_file = STRUCTURES_DIR / f"{struct_name}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for item in sorted(source.rglob("*")):
            rel = item.relative_to(source)

            if item.is_dir():
                f.write(f"DIR:{rel}\n")
            else:
                f.write(f"FILE:{rel}\n")

    print(f"Saved structure: {struct_name}")
    print(f"Location: {output_file}")
    return 0


def load_structure(struct_name, destination):
    structure_file = STRUCTURES_DIR / f"{struct_name}.txt"

    if not structure_file.exists():
        print(f"Structure '{struct_name}' not found.")
        return 1

    destination = Path(destination)

    with open(structure_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("DIR:"):
                path = destination / line[4:]
                path.mkdir(parents=True, exist_ok=True)

            elif line.startswith("FILE:"):
                path = destination / line[5:]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch(exist_ok=True)

    print(f"Created structure '{struct_name}' in:")
    print(destination.resolve())
    return 0


def savestruct_main():
    if len(sys.argv) != 3:
        print("Usage: savestruct <structname> <folder>")
        sys.exit(1)

    sys.exit(save_structure(sys.argv[1], sys.argv[2]))


def loadstruct_main():
    if len(sys.argv) != 3:
        print("Usage: loadstruct <structname> <destination>")
        sys.exit(1)

    sys.exit(load_structure(sys.argv[1], sys.argv[2]))