"""Project-local launcher for samirsaci/mcp-webscraper.

Keeps the MCP SDK version needed by this server in ./_vendor while reusing
Hermes' Python environment for shared packages such as requests/bs4/playwright.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENDOR = ROOT / "_vendor"
if VENDOR.exists():
    sys.path.insert(0, str(VENDOR))

runpy.run_path(str(ROOT / "scrapping.py"), run_name="__main__")
