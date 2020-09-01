import uvicorn

from fastapi import FastAPI


from quotable.routers import pinky_and_the_brain

app = FastAPI()
app.include_router(pinky_and_the_brain.router, prefix="")


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "quotable is up and running"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
