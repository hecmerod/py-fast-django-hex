import os

import django


def setup_django() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shared.django.config.django_settings")
    django.setup()
