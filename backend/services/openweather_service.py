from typing import Optional

api_key: Optional[str] = None


def get_report(
    city: str,
    state: Optional[str],
    country: Optional[str],
    units: Optional[str],
) -> dict:
    q = f"{city},{country}"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        f"q={q}&"
        f"appid={api_key}&"
        f"units={units}"
    )
    return {"url": url}
