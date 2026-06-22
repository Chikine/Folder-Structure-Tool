"""
Save command.

Handles:

    structtool save
"""

from utils.versioning import (
    get_next_version
)


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