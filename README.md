# StructTool

Save and recreate folder structures from the command line.

## Installation

Open a terminal in this project folder and run:

```bash
pip install .
```

This installs two commands:

```bash
savestruct
loadstruct
```

## Commands

### Save a structure

```bash
savestruct <structname> <folder>
```

Example:

```bash
savestruct website .
```

This scans the current folder and saves its structure as:

```text
~/.structtool/structures/website.txt
```

### Load a structure

```bash
loadstruct <structname> <destination>
```

Example:

```bash
loadstruct website ./NewProject
```

This recreates all folders and files in the destination.

## Where structures are stored

Windows:

```text
C:\Users\<username>\.structtool\structures
```

Linux/macOS:

```text
~/.structtool/structures
```

## Notes

- Creates empty files only.
- Preserves folder/file names and hierarchy.
- Existing folders are reused safely.
- Existing files are left untouched.