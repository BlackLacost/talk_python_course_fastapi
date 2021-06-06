from fastapi import APIRouter, Request, responses
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="backend/templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "home/index.html.j2", {"request": request}
    )


@router.get("/favicon.ico")
def favicon():
    return responses.RedirectResponse(url="/static/img/favicon.ico")
