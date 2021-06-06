from typing import Optional

import httpx

api_key: Optional[str] = None


async def get_report(
    city: str,
    state: Optional[str],
    country: Optional[str],
    units: Optional[str],
) -> dict:
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
    return forecast
