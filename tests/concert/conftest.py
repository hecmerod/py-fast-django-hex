from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import Mock

import pytest

from concert.domain.entities.concert import Concert


@pytest.fixture
def concert() -> Concert:
    now = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)
    return Concert(
        id=1,
        name="Summer Fest",
        artist="The Band",
        venue="Main Arena",
        starts_at=datetime(2026, 8, 15, 20, 0, tzinfo=UTC),
        price=Decimal("49.99"),
        created_at=now,
        updated_at=now,
    )


@pytest.fixture
def repository() -> Mock:
    return Mock()
