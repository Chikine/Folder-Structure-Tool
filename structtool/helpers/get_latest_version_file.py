from get_structure_dir import get_structure_dir

def get_latest_version_file(
    struct_name
):
    struct_dir = get_structure_dir(
        struct_name
    )

    versions = []

    for file in struct_dir.iterdir():

        if (
            file.is_file()
            and file.stem.startswith("v")
        ):

            try:
                version = int(
                    file.stem[1:]
                )

                versions.append(
                    (
                        version,
                        file
                    )
                )

            except ValueError:
                pass

    if not versions:
        return None

    versions.sort(
        key=lambda x: x[0]
    )

    return versions[-1][1]