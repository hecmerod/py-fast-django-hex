#!/usr/bin/env python3
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
env = os.environ.copy()
env.setdefault("PYTHONPYCACHEPREFIX", str(ROOT / ".pycache"))

os.execvpe(
    sys.executable,
    [
        sys.executable,
        "-m",
        "uvicorn",
        "main:app",
        "--app-dir",
        "src",
        "--reload",
        *sys.argv[1:],
    ],
    env,
)
