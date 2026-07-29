from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import Mock

import pytest

from concert.application.usecases.update_concert import UpdateConcertUseCase
from concert.domain.entities.concert import Concert
from concert.domain.errors.exceptions import ConcertNotFoundError


def test_execute_updates_concert_preserving_id_and_created_at(
    repository: Mock,
    concert: Concert,
) -> None:
    updated = Concert(
        id=concert.id,
        name="Updated Fest",
        artist="New Band",
        venue="New Arena",
        starts_at=datetime(2026, 9, 1, 20, 0, tzinfo=UTC),
        price=Decimal("59.99"),
        created_at=concert.created_at,
    )
    repository.get_by_id.return_value = concert
    repository.update.return_value = updated
    starts_at = datetime(2026, 9, 1, 20, 0, tzinfo=UTC)

    result = UpdateConcertUseCase(repository).execute(
        concert_id=1,
        name="Updated Fest",
        artist="New Band",
        venue="New Arena",
        starts_at=starts_at,
        price=Decimal("59.99"),
    )

    assert result == updated
    repository.get_by_id.assert_called_once_with(1)
    repository.update.assert_called_once()
    updated_arg = repository.update.call_args[0][0]
    assert updated_arg.id == 1
    assert updated_arg.created_at == concert.created_at


def test_execute_raises_when_concert_not_found(repository: Mock) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(ConcertNotFoundError, match="Concert 999 not found"):
        UpdateConcertUseCase(repository).execute(
            concert_id=999,
            name="Updated Fest",
            artist="New Band",
            venue="New Arena",
            starts_at=datetime(2026, 9, 1, 20, 0, tzinfo=UTC),
            price=Decimal("59.99"),
        )

    repository.update.assert_not_called()
