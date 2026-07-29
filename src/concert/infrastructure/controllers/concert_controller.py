from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from concert.domain.errors.exceptions import ConcertNotFoundError
from concert.application.usecases.create_concert import CreateConcertUseCase
from concert.application.usecases.delete_concert import DeleteConcertUseCase
from concert.application.usecases.get_concert import GetConcertUseCase
from concert.application.usecases.list_concerts import ListConcertsUseCase
from concert.application.usecases.update_concert import UpdateConcertUseCase
from concert.concert_dependencies import (
    get_create_concert_use_case,
    get_delete_concert_use_case,
    get_get_concert_use_case,
    get_list_concerts_use_case,
    get_update_concert_use_case,
)
from concert.domain.entities.concert import Concert
from concert.infrastructure.controllers.dtos.concert_response_dto import ConcertResponseDTO
from concert.infrastructure.controllers.dtos.create_concert_dto import ConcertCreateDTO
from concert.infrastructure.controllers.dtos.update_concert_dto import ConcertUpdateDTO

router = APIRouter(prefix="/concerts", tags=["concerts"])


def _to_response(concert: Concert) -> ConcertResponseDTO:
    return ConcertResponseDTO(
        id=concert.id,  # type: ignore[arg-type]
        name=concert.name,
        artist=concert.artist,
        venue=concert.venue,
        starts_at=concert.starts_at,
        price=concert.price,
        created_at=concert.created_at,  # type: ignore[arg-type]
        updated_at=concert.updated_at,  # type: ignore[arg-type]
    )


@router.get("", response_model=list[ConcertResponseDTO])
def list_concerts(
    use_case: Annotated[ListConcertsUseCase, Depends(get_list_concerts_use_case)],
) -> list[ConcertResponseDTO]:
    return [_to_response(concert) for concert in use_case.execute()]


@router.get("/{concert_id}", response_model=ConcertResponseDTO)
def get_concert(
    concert_id: int,
    use_case: Annotated[GetConcertUseCase, Depends(get_get_concert_use_case)],
) -> ConcertResponseDTO:
    try:
        return _to_response(use_case.execute(concert_id))
    except ConcertNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.post("", response_model=ConcertResponseDTO, status_code=status.HTTP_201_CREATED)
def create_concert(
    payload: ConcertCreateDTO,
    use_case: Annotated[CreateConcertUseCase, Depends(get_create_concert_use_case)],
) -> ConcertResponseDTO:
    concert = use_case.execute(
        name=payload.name,
        artist=payload.artist,
        venue=payload.venue,
        starts_at=payload.starts_at,
        price=payload.price,
    )
    return _to_response(concert)


@router.put("/{concert_id}", response_model=ConcertResponseDTO)
def update_concert(
    concert_id: int,
    payload: ConcertUpdateDTO,
    use_case: Annotated[UpdateConcertUseCase, Depends(get_update_concert_use_case)],
) -> ConcertResponseDTO:
    try:
        concert = use_case.execute(
            concert_id=concert_id,
            name=payload.name,
            artist=payload.artist,
            venue=payload.venue,
            starts_at=payload.starts_at,
            price=payload.price,
        )
    except ConcertNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    return _to_response(concert)


@router.delete("/{concert_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_concert(
    concert_id: int,
    use_case: Annotated[DeleteConcertUseCase, Depends(get_delete_concert_use_case)],
) -> None:
    try:
        use_case.execute(concert_id)
    except ConcertNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
