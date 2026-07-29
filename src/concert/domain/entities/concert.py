from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Concert:
    id: int | None
    name: str
    artist: str
    venue: str
    starts_at: datetime
    price: Decimal
    created_at: datetime | None = None
    updated_at: datetime | None = None
