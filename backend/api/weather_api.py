from typing import Optional

from fastapi import APIRouter, Depends

from models.location import Location
from services.openweather_service import get_report

router = APIRouter()


@router.get("/api/weather/{city}")
async def weather(
    loc: Location = Depends(),
    units: str = "metric",
):
    report = await get_report(loc.city, loc.state, loc.country, units)
    return report
