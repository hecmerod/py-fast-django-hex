#!/bin/sh
set -e

python manage.py migrate --noinput
exec uvicorn main:app --app-dir src --host 0.0.0.0 --port 8000
