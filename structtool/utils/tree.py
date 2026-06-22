import json
from .versioning import get_latest_version_file

def show_tree(
    struct_name
):
    version_file = (
        get_latest_version_file(
            struct_name
        )
    )

    if version_file is None:

        print(
            "Structure not found."
        )

        return 1

    if version_file.suffix != ".json":

        print(
            "Tree view only supports JSON structures."
        )

        return 1

    with open(
        version_file,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    for item in data["items"]:
        print(
            item["path"]
        )

    return 0