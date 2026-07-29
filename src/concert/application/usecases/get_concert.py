from concert.domain.errors.exceptions import ConcertNotFoundError
from concert.domain.entities.concert import Concert
from concert.domain.repositories.concert_repository import ConcertRepositoryPort


class GetConcertUseCase:
    def __init__(self, repository: ConcertRepositoryPort) -> None:
        self._repository = repository

    def execute(self, concert_id: int) -> Concert:
        concert = self._repository.get_by_id(concert_id)
        if concert is None:
            raise ConcertNotFoundError(f"Concert {concert_id} not found")
        return concert
