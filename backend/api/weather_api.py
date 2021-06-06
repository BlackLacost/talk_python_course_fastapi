from typing import Optional

from fastapi import APIRouter, Depends

from models.location import Location
from services.openweather_service import get_report

router = APIRouter()


@router.get("/api/weather/{city}")
def weather(
    loc: Location = Depends(),
    units: Optional[str] = "metric",
):
    report = get_report(loc.city, loc.state, loc.counter, units)
    return report