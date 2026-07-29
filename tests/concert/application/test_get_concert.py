from unittest.mock import Mock

import pytest

from concert.application.usecases.get_concert import GetConcertUseCase
from concert.domain.entities.concert import Concert
from concert.domain.errors.exceptions import ConcertNotFoundError


def test_execute_returns_concert(repository: Mock, concert: Concert) -> None:
    repository.get_by_id.return_value = concert

    result = GetConcertUseCase(repository).execute(1)

    assert result == concert
    repository.get_by_id.assert_called_once_with(1)


def test_execute_raises_when_concert_not_found(repository: Mock) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(ConcertNotFoundError, match="Concert 999 not found"):
        GetConcertUseCase(repository).execute(999)
