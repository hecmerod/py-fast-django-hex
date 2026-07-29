from unittest.mock import Mock

from concert.application.usecases.list_concerts import ListConcertsUseCase
from concert.domain.entities.concert import Concert


def test_execute_returns_all_concerts(repository: Mock, concert: Concert) -> None:
    repository.list_all.return_value = [concert]

    result = ListConcertsUseCase(repository).execute()

    assert result == [concert]
    repository.list_all.assert_called_once_with()


def test_execute_returns_empty_list(repository: Mock) -> None:
    repository.list_all.return_value = []

    result = ListConcertsUseCase(repository).execute()

    assert result == []
