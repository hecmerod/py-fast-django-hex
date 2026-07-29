from fastapi import FastAPI

from concert.infrastructure.controllers import concert_controller
from shared.healthcheck import healthcheck


def register_routes(app: FastAPI) -> None:
    app.include_router(concert_controller.router, prefix="/api")
    app.include_router(healthcheck.router)
