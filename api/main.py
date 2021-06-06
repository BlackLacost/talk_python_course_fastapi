import uvicorn
from fastapi import FastAPI
from uvicorn.config import LOG_LEVELS

api = FastAPI()


@api.get("/")
def index():
    return "Hello Wather app!"


if __name__ == "__main__":
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        log_level=LOG_LEVELS.get("info"),
        reload=True,
    )
