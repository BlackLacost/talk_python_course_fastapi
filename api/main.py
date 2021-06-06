from typing import Optional

import uvicorn
from fastapi import FastAPI, Response, responses
from uvicorn.config import LOG_LEVELS

api = FastAPI()


@api.get("/")
def index():
    body = (
        "<html>"
        "<body style='pagging: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>"
        "</div>"
        "</body>"
        "</html>"
    )
    return responses.HTMLResponse(content=body)


@api.get("/api/calculate")
async def cacluate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return responses.JSONResponse(
            content={"error": "Error: Z cannot be zero."},
            status_code=400,
        )
        # return Response(
        #     content='{"error": "Error: Z cannot be zero."}',
        #     media_type="application/json",
        #     status_code=400,
        # )
    value = x + y

    if z is not None:
        value /= z

    result = {"x": x, "y": y, "z": z, "value": value}
    return result


if __name__ == "__main__":
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        log_level=LOG_LEVELS.get("info"),
        reload=True,
    )
