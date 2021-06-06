from typing import Optional

from tools import weather_cache

import httpx

api_key: Optional[str] = None


async def get_report(
    city: str,
    state: Optional[str],
    country: str,
    units: str,
) -> dict:
    if forecast := weather_cache.get_weather(city, state, country, units):
        return forecast

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        f"q={q}&"
        f"appid={api_key}&"
        f"units={units}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    forecast = data.get("main", {})

    weather_cache.set_weather(city, state, country, units, forecast)
    return forecast
