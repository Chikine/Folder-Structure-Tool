"""
Load command.

Handles:

    structtool load
"""
from pathlib import Path
from ..utils import get_latest_version_file, load_structure_with_format

def load_structure(
    struct_name,
    destination
):
    """
    Recreate a structure
    into destination folder.

    Uses latest version.
    """
    version_file = (
        get_latest_version_file(
            struct_name
        )
    )

    if version_file is None:

        print(
            f"Structure '{struct_name}' not found."
        )

        return 1

    destination = Path(
        destination
    )

    if version_file.suffix == ".json":
        load_structure_with_format(
            version_file,
            destination,
            format='json'
        )

    else:
        load_structure_with_format(
            version_file,
            destination,
            format='txt'
        )

    print(
        f"Created '{struct_name}'"
    )

    return 0