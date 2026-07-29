from unittest.mock import Mock

import pytest

from concert.application.usecases.delete_concert import DeleteConcertUseCase
from concert.domain.entities.concert import Concert
from concert.domain.errors.exceptions import ConcertNotFoundError


def test_execute_deletes_concert(repository: Mock, concert: Concert) -> None:
    repository.get_by_id.return_value = concert

    DeleteConcertUseCase(repository).execute(1)

    repository.get_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(1)


def test_execute_raises_when_concert_not_found(repository: Mock) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(ConcertNotFoundError, match="Concert 999 not found"):
        DeleteConcertUseCase(repository).execute(999)

    repository.delete.assert_not_called()
