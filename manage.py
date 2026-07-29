#!/usr/bin/env python
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

if sys.pycache_prefix is None:
    sys.pycache_prefix = str(BASE_DIR / ".pycache")

sys.path.insert(0, str(BASE_DIR / "src"))


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shared.django.config.django_settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
