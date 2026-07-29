from concert.domain.errors.exceptions import ConcertNotFoundError
from concert.domain.repositories.concert_repository import ConcertRepositoryPort


class DeleteConcertUseCase:
    def __init__(self, repository: ConcertRepositoryPort) -> None:
        self._repository = repository

    def execute(self, concert_id: int) -> None:
        concert = self._repository.get_by_id(concert_id)
        if concert is None:
            raise ConcertNotFoundError(f"Concert {concert_id} not found")
        self._repository.delete(concert_id)
