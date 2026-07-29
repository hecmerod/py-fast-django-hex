from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ConcertResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    artist: str
    venue: str
    starts_at: datetime
    price: Decimal
    created_at: datetime
    updated_at: datetime
