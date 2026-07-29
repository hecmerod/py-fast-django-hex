from concert.domain.entities.concert import Concert
from concert.domain.repositories.concert_repository import ConcertRepositoryPort
from shared.django.models import ConcertModel


class DjangoConcertRepository(ConcertRepositoryPort):
    def _to_entity(self, model: ConcertModel) -> Concert:
        return Concert(
            id=model.pk,
            name=model.name,
            artist=model.artist,
            venue=model.venue,
            starts_at=model.starts_at,
            price=model.price,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    def list_all(self) -> list[Concert]:
        return [self._to_entity(model) for model in ConcertModel.objects.all()]

    def get_by_id(self, concert_id: int) -> Concert | None:
        try:
            model = ConcertModel.objects.get(pk=concert_id)
        except ConcertModel.DoesNotExist:
            return None
        return self._to_entity(model)

    def create(self, concert: Concert) -> Concert:
        model = ConcertModel.objects.create(
            name=concert.name,
            artist=concert.artist,
            venue=concert.venue,
            starts_at=concert.starts_at,
            price=concert.price,
        )
        return self._to_entity(model)

    def update(self, concert: Concert) -> Concert:
        model = ConcertModel.objects.get(pk=concert.id)
        model.name = concert.name
        model.artist = concert.artist
        model.venue = concert.venue
        model.starts_at = concert.starts_at
        model.price = concert.price
        model.save()
        return self._to_entity(model)

    def delete(self, concert_id: int) -> bool:
        deleted, _ = ConcertModel.objects.filter(pk=concert_id).delete()
        return deleted > 0
