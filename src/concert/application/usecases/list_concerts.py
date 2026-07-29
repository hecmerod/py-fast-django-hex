from concert.domain.entities.concert import Concert
from concert.domain.repositories.concert_repository import ConcertRepositoryPort


class ListConcertsUseCase:
    def __init__(self, repository: ConcertRepositoryPort) -> None:
        self._repository = repository

    def execute(self) -> list[Concert]:
        return self._repository.list_all()
