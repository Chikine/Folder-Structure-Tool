# StructTool

StructTool is a command-line tool that saves and recreates folder structures.

It can be used as a lightweight project template manager, allowing you to:

- Save folder structures
- Recreate structures later
- Store multiple versions
- Save file contents (optional)
- Organize templates using tags
- Search templates by tag
- Display structure trees
- Store templates as JSON or TXT

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Initialize a Project](#initialize-a-project)
  - [`.structignore`](#structignore)
  - [`.structtool.json`](#structtooljson)
  - [Recreate Configuration Files](#recreate-configuration-files)
  - [Recommended Workflow](#recommended-workflow)
- [Commands](#commands)
  - [Save a Structure](#save-a-structure)
  - [Save as JSON](#save-as-json)
  - [Save as TXT](#save-as-txt)
  - [Save File Contents](#save-file-contents)
  - [Ignore Files and Folders](#ignore-files-and-folders)
  - [Add Tags](#add-tags)
- [Load a Structure](#load-a-structure)
- [List Structures](#list-structures)
- [Remove a Structure](#remove-a-structure)
- [Show Version History](#show-version-history)
- [Search by Tag](#search-by-tag)
- [Tree View](#tree-view)
- [Versioning](#versioning)
- [Storage Location](#storage-location)
  - [Windows](#windows)
  - [Linux](#linux)
  - [macOS](#macos)
- [Structure Layout](#structure-layout)
- [JSON Structure Format](#json-structure-format)
- [Roadmap](#roadmap)
- [Development](#development)
- [Command Table](#command-table)
- [License](#license)

## Features

✅ Save folder structures

✅ Recreate structures

✅ JSON and TXT formats

✅ Optional file content storage

✅ Structure versioning

✅ Tags and categories

✅ Search by tag

✅ Tree visualization

✅ Ignore files and folders

✅ Cross-platform support

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Chikine/Folder-Structure-Tool

cd structtool
```

Install locally:

```bash
pip install .
```

Verify installation:

```bash
structtool --help
```

---

## Initialize a Project

Before saving structures, initialize StructTool in your project:

```bash
structtool init
```

This creates two configuration files:

```text
.structignore
.structtool.json
```

---

### `.structignore`

Defines files and folders that should not be saved.

Example:

```text
# Node.js
node_modules
dist

# Python
__pycache__
*.pyc

# Git
.git

# IDE
.vscode
.idea
```

These patterns are automatically applied when running:

```bash
structtool save website .
```

---

### `.structtool.json`

Stores default StructTool settings.

Example:

```json
{
    "default_format": "json",
    "include_content": false,
    "ignore_file": ".structignore",
    "default_tags": [],
    "max_content_size_kb": 100
}
```

This allows `structtool save` to reuse project settings without repeatedly specifying command-line options.

---

### Recreate Configuration Files

If configuration files already exist, StructTool will preserve them:

```bash
structtool init
```

To overwrite existing files:

```bash
structtool init --force
```

---

### Recommended Workflow

```bash
# Initialize configuration
structtool init

# Save the current project
structtool save website .

# Show available structures
structtool list

# Load the structure elsewhere
structtool load website ./NewProject
```

---

## Commands

### Save a Structure

Save a folder structure:

```bash
structtool save website .
```

---

### Save as JSON

```bash
structtool save website . --format json
```

---

### Save as TXT

```bash
structtool save website . --format txt
```

---

### Save File Contents

By default only folder/file names are stored.

To save file contents:

```bash
structtool save website . --include-content
```

Example:

```bash
structtool save react-app . \
    --format json \
    --include-content
```

---

### Ignore Files and Folders

Ignore specific paths while saving:

```bash
structtool save website . \
    --ignore node_modules .git dist
```

Example:

```bash
structtool save website . \
    --ignore node_modules .git __pycache__
```

---

### Add Tags

Attach tags to structures:

```bash
structtool save react-app . \
    --tags react frontend vite
```

Metadata example:

```json
{
    "name": "react-app",
    "tags": [
        "react",
        "frontend",
        "vite"
    ],
    "latest_version": 1
}
```

---

## Load a Structure

Load the latest version of a structure:

```bash
structtool load website ./NewProject
```

Result:

```text
NewProject/
├── src/
├── public/
└── package.json
```

---

## List Structures

Display all saved structures:

```bash
structtool list
```

Example:

```text
react-app
website
api-server
```

---

## Remove a Structure

Delete a structure and all versions:

```bash
structtool remove website
```

---

## Show Version History

Display saved versions:

```bash
structtool history website
```

Example:

```text
v1.json
v2.json
v3.json
```

---

## Search by Tag

Search structures using tags:

```bash
structtool search react
```

Example:

```text
react-app
react-dashboard
react-admin
```

---

## Tree View

Display a saved structure:

```bash
structtool show website
```

Example:

```text
src
├── components
├── pages
├── App.jsx
└── main.jsx

public
└── favicon.ico
```

---

## Versioning

Each save creates a new version automatically.

Example:

```bash
structtool save website .
```

Creates:

```text
v1.json
```

Saving again:

```bash
structtool save website .
```

Creates:

```text
v2.json
```

Saving again:

```bash
structtool save website .
```

Creates:

```text
v3.json
```

Latest version is automatically used when loading.

---

## Storage Location

### Windows

```text
C:\Users\<username>\.structtool\structures
```

### Linux

```text
~/.structtool/structures
```

### macOS

```text
~/.structtool/structures
```

---

## Structure Layout

Example:

```text
.structtool/
└── structures/
    └── website/
        ├── metadata.json
        ├── v1.json
        ├── v2.json
        └── v3.txt
```

Metadata:

```json
{
    "name": "website",
    "tags": [
        "frontend",
        "react"
    ],
    "latest_version": 3
}
```

---

## JSON Structure Format

Example:

```json
{
    "format": "json",
    "include_content": true,
    "items": [
        {
            "type": "dir",
            "path": "src"
        },
        {
            "type": "file",
            "path": "src/App.jsx",
            "content": "export default function App() {}"
        }
    ]
}
```

---

## Roadmap

Planned features:

- [ ] Export structures
- [ ] Import structures
- [ ] Structure diff
- [ ] Structure validation
- [ ] Remote template repositories
- [ ] .structignore support
- [ ] Interactive project wizard
- [ ] Better tree rendering

---

## Development

Run from source:

```bash
python -m structtool.cli
```

Install editable version:

```bash
pip install -e .
```

---

## Command Table

| Command              | Description                                   |
| -------------------- | --------------------------------------------- |
| `structtool init`    | Create `.structignore` and `.structtool.json` |
| `structtool save`    | Save a folder structure                       |
| `structtool load`    | Recreate a structure                          |
| `structtool list`    | Show saved structures                         |
| `structtool history` | Show version history                          |
| `structtool show`    | Display structure tree                        |
| `structtool search`  | Search by tags                                |
| `structtool remove`  | Delete a structure                            |

---

## License

MIT License