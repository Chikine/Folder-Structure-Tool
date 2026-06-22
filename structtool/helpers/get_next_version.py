from get_structure_dir import get_structure_dir

def get_next_version(
    struct_name
):
    struct_dir = get_structure_dir(
        struct_name
    )

    if not struct_dir.exists():
        return 1

    versions = []

    for file in struct_dir.iterdir():

        if file.stem.startswith("v"):

            try:
                versions.append(
                    int(file.stem[1:])
                )
            except ValueError:
                pass

    return (
        max(versions, default=0)
        + 1
    )