from functools import lru_cache

from concert.application.usecases.create_concert import CreateConcertUseCase
from concert.application.usecases.delete_concert import DeleteConcertUseCase
from concert.application.usecases.get_concert import GetConcertUseCase
from concert.application.usecases.list_concerts import ListConcertsUseCase
from concert.application.usecases.update_concert import UpdateConcertUseCase


@lru_cache
def _get_concert_repository():
    from concert.infrastructure.repositories.concert_repository import DjangoConcertRepository

    return DjangoConcertRepository()


def get_list_concerts_use_case() -> ListConcertsUseCase:
    return ListConcertsUseCase(repository=_get_concert_repository())


def get_get_concert_use_case() -> GetConcertUseCase:
    return GetConcertUseCase(repository=_get_concert_repository())


def get_create_concert_use_case() -> CreateConcertUseCase:
    return CreateConcertUseCase(repository=_get_concert_repository())


def get_update_concert_use_case() -> UpdateConcertUseCase:
    return UpdateConcertUseCase(repository=_get_concert_repository())


def get_delete_concert_use_case() -> DeleteConcertUseCase:
    return DeleteConcertUseCase(repository=_get_concert_repository())
