"""
File format handlers.

Responsible for:
- saving json structures
- saving txt structures
- loading json structures
- loading txt structures
"""
import json

from ..helpers import should_ignore

def save_structure_with_format(source, output_file, ignore_patterns, include_content, format = 'txt'):
    """
    *support format: 'json' , 'txt'*

    Parameters
    ----------
    source : Path
        Folder to scan.

    output_file : Path
        Destination txt file.

    ignore_patterns : list[str]
        Paths to ignore.

    include_content : bool
        Whether file contents should
        be stored.

    TXT format example:

        DIR:src

        FILE:src/main.py
        CONTENT_START
        print("hello")
        CONTENT_END

    JSON format example:

        {
            "format": "json",
            "items": [
                {
                    "type": "dir",
                    "path": "src"
                },
                {
                    "type": "file",
                    "path": "src/main.py",
                    "content": "print('hello')"
                }
            ]
        }
    """
    
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
    
    if format == 'txt':
        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:
            for item in sorted(source.rglob("*")):

                rel = item.relative_to(source)
                rel_str = str(rel)

                if should_ignore(
                    rel_str,
                    ignore_patterns
                ):
                    continue

                if item.is_dir():

                    f.write(
                        f"DIR:{rel_str}\n"
                    )

                else:

                    f.write(
                        f"FILE:{rel_str}\n"
                    )

                    if include_content:

                        try:

                            content = item.read_text(
                                encoding="utf-8"
                            )

                        except Exception:
                            content = ""

                        f.write(
                            "CONTENT_START\n"
                        )

                        f.write(content)

                        if (
                            content
                            and
                            not content.endswith("\n")
                        ):
                            f.write("\n")

                        f.write(
                            "CONTENT_END\n"
                        )

def load_structure_with_format(version_file, destination, format='txt'):
    """
    *support format: 'json' , 'txt'*

    **Restore folders and files from
    a structure**

    TXT files supports restoring file 
    contents saved between:
        CONTENT_START
        ...
        CONTENT_END

    JSON files containing a "content"
    field will be recreated with
    their original contents.

    Otherwise an empty file is
    created.
    """

    if format == 'json':
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

    if format == 'txt':
        with open(
            version_file,
            "r",
            encoding="utf-8"
        ) as f:

            lines = f.readlines()

        i = 0

        while i < len(lines):

            line = lines[i].rstrip("\n")

            if line.startswith("DIR:"):

                path = (
                    destination /
                    line[4:]
                )

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                i += 1

            elif line.startswith("FILE:"):

                path = (
                    destination /
                    line[5:]
                )

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                content = ""

                i += 1

                if (
                    i < len(lines)
                    and
                    lines[i].strip()
                    == "CONTENT_START"
                ):

                    i += 1

                    content_lines = []

                    while (
                        i < len(lines)
                        and
                        lines[i].strip()
                        != "CONTENT_END"
                    ):

                        content_lines.append(
                            lines[i]
                        )

                        i += 1

                    content = "".join(
                        content_lines
                    )

                    i += 1

                if content:

                    path.write_text(
                        content,
                        encoding="utf-8"
                    )

                else:

                    path.touch(
                        exist_ok=True
                    )

            else:

                i += 1