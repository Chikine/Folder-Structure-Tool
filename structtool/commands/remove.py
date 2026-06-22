"""
Remove command.

Handles:

    structtool remove
"""
import shutil

from ..helpers import get_structure_dir

def remove_structure(
    struct_name
):
    """
    Delete a structure and
    all versions.
    """
    struct_dir = (
        get_structure_dir(
            struct_name
        )
    )

    if not struct_dir.exists():

        print(
            "Structure not found."
        )

        return 1

    shutil.rmtree(
        struct_dir
    )

    print(
        f"Removed '{struct_name}'"
    )

    return 0