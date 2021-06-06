import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from uvicorn.config import LOG_LEVELS

from api import weather_api
from views import home

api = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    api.mount(
        "/static", StaticFiles(directory="backend/static"), name="static"
    )
    api.include_router(home.router)
    api.include_router(weather_api.router)


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
