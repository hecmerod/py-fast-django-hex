from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from concert.concert_dependencies import (
    get_create_concert_use_case,
    get_delete_concert_use_case,
    get_get_concert_use_case,
    get_list_concerts_use_case,
    get_update_concert_use_case,
)
from concert.domain.entities.concert import Concert
from concert.domain.errors.exceptions import ConcertNotFoundError
from concert.infrastructure.controllers import concert_controller


@pytest.fixture
def client() -> TestClient:
    app = FastAPI()
    app.include_router(concert_controller.router, prefix="/api")
    return TestClient(app)


def _override(client: TestClient, dependency, use_case: Mock) -> None:
    client.app.dependency_overrides[dependency] = lambda: use_case


def test_list_concerts_returns_200(client: TestClient, concert: Concert) -> None:
    use_case = Mock()
    use_case.execute.return_value = [concert]
    _override(client, get_list_concerts_use_case, use_case)

    response = client.get("/api/concerts")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Summer Fest",
            "artist": "The Band",
            "venue": "Main Arena",
            "starts_at": "2026-08-15T20:00:00Z",
            "price": "49.99",
            "created_at": "2026-01-01T12:00:00Z",
            "updated_at": "2026-01-01T12:00:00Z",
        }
    ]


def test_get_concert_returns_200(client: TestClient, concert: Concert) -> None:
    use_case = Mock()
    use_case.execute.return_value = concert
    _override(client, get_get_concert_use_case, use_case)

    response = client.get("/api/concerts/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Summer Fest"
    use_case.execute.assert_called_once_with(1)


def test_get_concert_returns_404_when_not_found(client: TestClient) -> None:
    use_case = Mock()
    use_case.execute.side_effect = ConcertNotFoundError("Concert 999 not found")
    _override(client, get_get_concert_use_case, use_case)

    response = client.get("/api/concerts/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Concert 999 not found"


def test_create_concert_returns_201(client: TestClient, concert: Concert) -> None:
    use_case = Mock()
    use_case.execute.return_value = concert
    _override(client, get_create_concert_use_case, use_case)

    response = client.post(
        "/api/concerts",
        json={
            "name": "Summer Fest",
            "artist": "The Band",
            "venue": "Main Arena",
            "starts_at": "2026-08-15T20:00:00Z",
            "price": "49.99",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    use_case.execute.assert_called_once()


def test_update_concert_returns_200(client: TestClient, concert: Concert) -> None:
    use_case = Mock()
    use_case.execute.return_value = concert
    _override(client, get_update_concert_use_case, use_case)

    response = client.put(
        "/api/concerts/1",
        json={
            "name": "Summer Fest",
            "artist": "The Band",
            "venue": "Main Arena",
            "starts_at": "2026-08-15T20:00:00Z",
            "price": "49.99",
        },
    )

    assert response.status_code == 200
    use_case.execute.assert_called_once()


def test_update_concert_returns_404_when_not_found(client: TestClient) -> None:
    use_case = Mock()
    use_case.execute.side_effect = ConcertNotFoundError("Concert 999 not found")
    _override(client, get_update_concert_use_case, use_case)

    response = client.put(
        "/api/concerts/999",
        json={
            "name": "Summer Fest",
            "artist": "The Band",
            "venue": "Main Arena",
            "starts_at": "2026-08-15T20:00:00Z",
            "price": "49.99",
        },
    )

    assert response.status_code == 404


def test_delete_concert_returns_204(client: TestClient) -> None:
    use_case = Mock()
    _override(client, get_delete_concert_use_case, use_case)

    response = client.delete("/api/concerts/1")

    assert response.status_code == 204
    use_case.execute.assert_called_once_with(1)


def test_delete_concert_returns_404_when_not_found(client: TestClient) -> None:
    use_case = Mock()
    use_case.execute.side_effect = ConcertNotFoundError("Concert 999 not found")
    _override(client, get_delete_concert_use_case, use_case)

    response = client.delete("/api/concerts/999")

    assert response.status_code == 404
