"""Build the HTML docs and open them in the default browser.

Run with the venv interpreter, e.g.:

    venv/bin/python preview.py
"""

import pathlib
import subprocess
import sys
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent

subprocess.run(
    [sys.executable, "-m", "sphinx", "-M", "html", ".", "_build"],
    cwd=ROOT,
    check=True,
)

webbrowser.open((ROOT / "_build" / "html" / "index.html").as_uri())
