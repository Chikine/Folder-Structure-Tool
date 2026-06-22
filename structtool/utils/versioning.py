"""
Version management helpers.

Responsible for:
- determining next version
- locating latest version
"""

from constants import STRUCTURES_DIR


def get_structure_dir(
    struct_name
):
    """
    Return the folder that stores
    a structure's versions.
    """
    return (
        STRUCTURES_DIR /
        struct_name
    )


def get_next_version(
    struct_name
):
    """
    Calculate next version number.

    Example:

    Existing:
        v1.json
        v2.json

    Returns:
        3
    """