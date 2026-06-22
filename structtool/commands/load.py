"""
Load command.

Handles:

    structtool load
"""
import json

from pathlib import Path
from ..helpers import get_latest_version_file

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

        with open(
            version_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        for item in data["items"]:

            path = (
                destination /
                item["path"]
            )

            if item["type"] == "dir":

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

            else:

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                if (
                    "content"
                    in item
                ):

                    path.write_text(
                        item["content"],
                        encoding="utf-8"
                    )

                else:

                    path.touch(
                        exist_ok=True
                    )

    else:

        with open(
            version_file,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                line = line.strip()

                if line.startswith(
                    "DIR:"
                ):

                    path = (
                        destination /
                        line[4:]
                    )

                    path.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                elif line.startswith(
                    "FILE:"
                ):

                    path = (
                        destination /
                        line[5:]
                    )

                    path.parent.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                    path.touch(
                        exist_ok=True
                    )

    print(
        f"Created '{struct_name}'"
    )

    return 0