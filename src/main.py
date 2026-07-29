import sys
from pathlib import Path

if sys.pycache_prefix is None:
    _root = Path(__file__).resolve().parent.parent
    sys.pycache_prefix = str(_root / ".pycache")

from contextlib import asynccontextmanager
from fastapi import FastAPI
from shared.django.django_setup import setup_django

setup_django()

from router import register_routes  # noqa: E402


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


app = FastAPI(
    title="Fever Interview API",
    description="Hexagonal architecture API with FastAPI and Django ORM",
    version="0.1.0",
    lifespan=lifespan,
)

register_routes(app)
