from pathlib import Path
import json

def init_project(force=False):
    """
    Initialize StructTool configuration files in the current directory.

    Creates:

        .structignore
        .structtool.json

    Existing files are preserved unless force=True.

    Parameters
    ----------
    force : bool, default=False
        Whether existing configuration files should be overwritten.

    Returns
    -------
    int
        0 if successful.
    """

    current_dir = Path.cwd()

    structignore_path = current_dir / ".structignore"
    config_path = current_dir / ".structtool.json"

    default_structignore = """# Node.js
node_modules
dist
coverage

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.venv

# Git
.git

# IDE
.vscode
.idea

# OS files
.DS_Store
Thumbs.db

# Build
build

# Logs
*.log
"""

    default_config = {
        "default_format": "json",
        "include_content": False,
        "ignore_file": ".structignore",
        "default_tags": [],
        "max_content_size_kb": 100
    }

    created_files = []
    skipped_files = []

    #
    # Create .structignore
    #
    if force or not structignore_path.exists():

        structignore_path.write_text(
            default_structignore,
            encoding="utf-8"
        )

        created_files.append(".structignore")

    else:
        skipped_files.append(".structignore")

    #
    # Create .structtool.json
    #
    if force or not config_path.exists():

        with open(
            config_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                default_config,
                f,
                indent=4,
                ensure_ascii=False
            )

        created_files.append(".structtool.json")

    else:
        skipped_files.append(".structtool.json")

    print("Initialized StructTool configuration.\n")

    if created_files:

        print("Created:")

        for file in created_files:
            print(f"  ✓ {file}")

    if skipped_files:

        print("\nSkipped (already exists):")

        for file in skipped_files:
            print(f"  • {file}")

    return 0