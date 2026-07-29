from datetime import datetime
from decimal import Decimal

from concert.domain.entities.concert import Concert
from concert.domain.repositories.concert_repository import ConcertRepositoryPort


class CreateConcertUseCase:
    def __init__(self, repository: ConcertRepositoryPort) -> None:
        self._repository = repository

    def execute(
        self,
        name: str,
        artist: str,
        venue: str,
        starts_at: datetime,
        price: Decimal,
    ) -> Concert:
        concert = Concert(
            id=None,
            name=name,
            artist=artist,
            venue=venue,
            starts_at=starts_at,
            price=price,
        )
        return self._repository.create(concert)
