import json
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from uvicorn.config import LOG_LEVELS

from api import weather_api
from services import openweather_service
from views import home

api = FastAPI()


def configure():
    configure_routing()
    configure_apikeys()


def configure_routing():
    api.mount(
        "/static", StaticFiles(directory="backend/static"), name="static"
    )
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_apikeys():
    file = Path("backend/settings.json").absolute()
    if not file.exists():
        print(
            f"WARNING: {file} file not found, you cannot continue, "
            "please see settihngs_template.json"
        )
        raise Exception(
            "settings.json file not found, you cannot continue, "
            "please see settings_template."
        )

    with open(file) as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get("api_key")


if __name__ == "__main__":
    configure()
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        log_level=LOG_LEVELS.get("info"),
        reload=True,
    )
else:
    configure()
