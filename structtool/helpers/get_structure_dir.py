from pathlib import Path

APP_DIR = Path.home() / ".structtool"
STRUCTURES_DIR = APP_DIR / "structures"

STRUCTURES_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def get_structure_dir(
    struct_name
):
    return (
        STRUCTURES_DIR /
        struct_name
    )