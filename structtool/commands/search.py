"""
Search command.

Handles:

    structtool search
"""
import json

from ..constants import STRUCTURES_DIR

def search_by_tag(
    tag
):
    """
    Search structures by tag.

    Example:

        structtool search react
    """
    for struct_dir in (
        STRUCTURES_DIR.iterdir()
    ):

        metadata_file = (
            struct_dir /
            "metadata.json"
        )

        if (
            not metadata_file.exists()
        ):
            continue

        metadata = json.loads(
            metadata_file.read_text(
                encoding="utf-8"
            )
        )

        if tag in metadata.get(
            "tags",
            []
        ):

            print(
                struct_dir.name
            )

    return 0