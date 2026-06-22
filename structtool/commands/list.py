"""
List command.

Handles:

    structtool list
"""

from constants import STRUCTURES_DIR

def list_structures():
    """
    Print all available
    structure names.
    """
    if not STRUCTURES_DIR.exists():
        return 0

    for item in sorted(
        STRUCTURES_DIR.iterdir()
    ):

        if item.is_dir():
            print(
                item.name
            )

    return 0