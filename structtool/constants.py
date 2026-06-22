"""
Application-wide constants.

This file contains paths used by StructTool.
"""

from pathlib import Path

APP_DIR = Path.home() / ".structtool"

STRUCTURES_DIR = (
    APP_DIR /
    "structures"
)

STRUCTURES_DIR.mkdir(
    parents=True,
    exist_ok=True
)