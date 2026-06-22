"""
History command.

Handles:

    structtool history
"""
from ..helpers import get_structure_dir

def show_history(
    struct_name
):
    """
    Display all saved
    versions.

    Example:

        v1.json
        v2.json
        v3.json
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

    for file in sorted(
        struct_dir.glob("v*.*")
    ):
        print(
            file.name
        )

    return 0