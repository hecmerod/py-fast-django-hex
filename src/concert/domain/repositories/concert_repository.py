from abc import ABC, abstractmethod

from concert.domain.entities.concert import Concert


class ConcertRepositoryPort(ABC):
    @abstractmethod
    def list_all(self) -> list[Concert]:
        pass

    @abstractmethod
    def get_by_id(self, concert_id: int) -> Concert | None:
        pass

    @abstractmethod
    def create(self, concert: Concert) -> Concert:
        pass

    @abstractmethod
    def update(self, concert: Concert) -> Concert:
        pass

    @abstractmethod
    def delete(self, concert_id: int) -> bool:
        pass
