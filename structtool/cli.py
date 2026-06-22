"""
CLI entrypoint.

Responsible only for:
- parsing arguments
- dispatching commands
"""

import argparse
import sys

from commands.save import (
    save_structure
)

from commands.load import (
    load_structure
)

from commands.list import (
    list_structures
)

from commands.remove import (
    remove_structure
)

from commands.history import (
    show_history
)

from commands.search import (
    search_by_tag
)

from utils.tree import (
    show_tree
)

def main():
    """
    Main CLI entrypoint.

    Parses command-line arguments
    and executes requested command.
    """
    parser = argparse.ArgumentParser(
        prog="structtool",
        description=(
            "Save and recreate folder structures"
        )
    )

    subparsers = (
        parser.add_subparsers(
            dest="command"
        )
    )

    # Save
    save_parser = (
        subparsers.add_parser(
            "save"
        )
    )

    save_parser.add_argument(
        "name"
    )

    save_parser.add_argument(
        "folder"
    )

    save_parser.add_argument(
        "--format",
        choices=[
            "json",
            "txt"
        ],
        default="json"
    )

    save_parser.add_argument(
        "--include-content",
        action="store_true"
    )

    save_parser.add_argument(
        "--ignore",
        nargs="*",
        default=[]
    )

    save_parser.add_argument(
        "--tags",
        nargs="*",
        default=[]
    )

    # Load
    load_parser = (
        subparsers.add_parser(
            "load"
        )
    )

    load_parser.add_argument(
        "name"
    )

    load_parser.add_argument(
        "destination"
    )

    # List
    subparsers.add_parser(
        "list"
    )

    # Remove
    remove_parser = (
        subparsers.add_parser(
            "remove"
        )
    )

    remove_parser.add_argument(
        "name"
    )

    # History
    history_parser = (
        subparsers.add_parser(
            "history"
        )
    )

    history_parser.add_argument(
        "name"
    )

    # Search
    search_parser = (
        subparsers.add_parser(
            "search"
        )
    )

    search_parser.add_argument(
        "tag"
    )

    # Show
    show_parser = (
        subparsers.add_parser(
            "show"
        )
    )

    show_parser.add_argument(
        "name"
    )

    args = parser.parse_args()

    if args.command == "save":

        sys.exit(
            save_structure(
                args.name,
                args.folder,
                args.format,
                args.include_content,
                args.ignore,
                args.tags
            )
        )

    elif args.command == "load":

        sys.exit(
            load_structure(
                args.name,
                args.destination
            )
        )

    elif args.command == "list":

        sys.exit(
            list_structures()
        )

    elif args.command == "remove":

        sys.exit(
            remove_structure(
                args.name
            )
        )

    elif args.command == "history":

        sys.exit(
            show_history(
                args.name
            )
        )

    elif args.command == "search":

        sys.exit(
            search_by_tag(
                args.tag
            )
        )

    elif args.command == "show":

        sys.exit(
            show_tree(
                args.name
            )
        )

    else:
        parser.print_help()