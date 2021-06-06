import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from uvicorn.config import LOG_LEVELS

api = FastAPI()
templates = Jinja2Templates(directory="api/templates")


@api.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "home/index.html.j2", {"request": request}
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        log_level=LOG_LEVELS.get("info"),
        reload=True,
    )
