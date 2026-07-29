from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import Mock

from concert.application.usecases.create_concert import CreateConcertUseCase
from concert.domain.entities.concert import Concert


def test_execute_creates_concert_via_repository(repository: Mock, concert: Concert) -> None:
    repository.create.return_value = concert
    starts_at = datetime(2026, 8, 15, 20, 0, tzinfo=UTC)

    result = CreateConcertUseCase(repository).execute(
        name="Summer Fest",
        artist="The Band",
        venue="Main Arena",
        starts_at=starts_at,
        price=Decimal("49.99"),
    )

    assert result == concert
    repository.create.assert_called_once()
    created = repository.create.call_args[0][0]
    assert created == Concert(
        id=None,
        name="Summer Fest",
        artist="The Band",
        venue="Main Arena",
        starts_at=starts_at,
        price=Decimal("49.99"),
    )
