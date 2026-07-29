from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class ConcertUpdateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    artist: str = Field(min_length=1, max_length=255)
    venue: str = Field(min_length=1, max_length=255)
    starts_at: datetime
    price: Decimal = Field(gt=0, decimal_places=2)