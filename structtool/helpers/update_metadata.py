import json
from ..helpers.get_metadata_file import get_metadata_file
from ..helpers.get_structure_dir import get_structure_dir

def update_metadata(
    struct_name,
    tags,
    version
):
    struct_dir = get_structure_dir(
        struct_name
    )

    struct_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    metadata = {
        "name": struct_name,
        "tags": tags,
        "latest_version": version
    }

    with open(
        get_metadata_file(
            struct_name
        ),
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            metadata,
            f,
            indent=4,
            ensure_ascii=False
        )