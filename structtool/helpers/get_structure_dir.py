from pathlib import Path

from constants import STRUCTURES_DIR

def get_structure_dir(
    struct_name
):
    return (
        STRUCTURES_DIR /
        struct_name
    )