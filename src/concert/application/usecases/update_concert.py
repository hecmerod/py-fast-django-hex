from datetime import datetime
from decimal import Decimal

from concert.domain.errors.exceptions import ConcertNotFoundError
from concert.domain.entities.concert import Concert
from concert.domain.repositories.concert_repository import ConcertRepositoryPort


class UpdateConcertUseCase:
    def __init__(self, repository: ConcertRepositoryPort) -> None:
        self._repository = repository

    def execute(
        self,
        concert_id: int,
        name: str,
        artist: str,
        venue: str,
        starts_at: datetime,
        price: Decimal,
    ) -> Concert:
        existing = self._repository.get_by_id(concert_id)
        if existing is None:
            raise ConcertNotFoundError(f"Concert {concert_id} not found")
        updated = Concert(
            id=existing.id,
            name=name,
            artist=artist,
            venue=venue,
            starts_at=starts_at,
            price=price,
            created_at=existing.created_at,
        )
        return self._repository.update(updated)
