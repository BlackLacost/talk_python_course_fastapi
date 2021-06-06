from typing import Optional

from fastapi import APIRouter, Depends

from models.location import Location

router = APIRouter()


@router.get("/api/weather/{city}")
def weather(
    loc: Location = Depends(),
    units: Optional[str] = "metric",
):
    return f"{loc.city}, {loc.state}, {loc.counter}, {units}"
