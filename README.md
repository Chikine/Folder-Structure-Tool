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
git clone https://github.com/yourusername/structtool.git

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

## License

MIT License