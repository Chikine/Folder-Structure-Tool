from pathlib import Path
import json

"""
Save command.

Handles:

    structtool save
"""

from utils.versioning import (
    get_next_version
)

from ..helpers import get_structure_dir, should_ignore, update_metadata

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

    if format == "json":

        data = {
            "format": "json",
            "include_content": include_content,
            "items": []
        }

        for item in sorted(
            source.rglob("*")
        ):

            rel = item.relative_to(
                source
            )

            rel_str = str(rel)

            if should_ignore(
                rel_str,
                ignore_patterns
            ):
                continue

            if item.is_dir():

                data["items"].append({
                    "type": "dir",
                    "path": rel_str
                })

            else:

                entry = {
                    "type": "file",
                    "path": rel_str
                }

                if include_content:

                    try:
                        entry[
                            "content"
                        ] = item.read_text(
                            encoding="utf-8"
                        )

                    except Exception:
                        entry[
                            "content"
                        ] = ""

                data["items"].append(
                    entry
                )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    else:

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            for item in sorted(
                source.rglob("*")
            ):

                rel = item.relative_to(
                    source
                )

                rel_str = str(rel)

                if should_ignore(
                    rel_str,
                    ignore_patterns
                ):
                    continue

                if item.is_dir():
                    f.write(
                        f"DIR:{rel}\n"
                    )

                else:
                    f.write(
                        f"FILE:{rel}\n"
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