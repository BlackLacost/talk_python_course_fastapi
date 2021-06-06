from fastapi import APIRouter

router = APIRouter()


@router.get("/api/weather")
def weather():
    return "Some report"
