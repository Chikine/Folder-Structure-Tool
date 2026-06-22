"""
Save command.

Handles:

    structtool save
"""
from pathlib import Path
from ..helpers import get_structure_dir
from ..utils import update_metadata, get_next_version, save_structure_with_format

def save_structure(
    struct_name,
    source_folder,
    format="json",
    include_content=False,
    ignore_patterns=None,
    tags=None
):
    """
    Save a folder structure.

    Creates:

        metadata.json

        v1.json
        v2.json

    depending on version.
    """
    ignore_patterns = (
        ignore_patterns or []
    )

    tags = tags or []

    source = Path(
        source_folder
    )

    if not source.exists():
        print(
            f"Error: '{source}' does not exist."
        )
        return 1

    struct_dir = get_structure_dir(
        struct_name
    )

    struct_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    version = get_next_version(
        struct_name
    )

    output_file = (
        struct_dir /
        f"v{version}.{format}"
    )

    save_structure_with_format(
        source,
        output_file,
        ignore_patterns,
        include_content,
        format
    )

    update_metadata(
        struct_name,
        tags,
        version
    )

    print(
        f"Saved '{struct_name}'"
    )

    print(
        f"Version: v{version}"
    )

    return 0