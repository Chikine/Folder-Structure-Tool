from .get_structure_dir import get_structure_dir

def get_metadata_file(
    struct_name
):
    return (
        get_structure_dir(struct_name)
        / "metadata.json"
    )