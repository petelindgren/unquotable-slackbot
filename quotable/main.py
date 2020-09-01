import random

import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from quotable.routers import pinky_and_the_brain
from quotable.routers import futurama

app = FastAPI()
app.include_router(pinky_and_the_brain.router, prefix="")
app.include_router(futurama.router, prefix="")

quote_engines = [pinky_and_the_brain.generate_quote, futurama.generate_quote]


@app.get("/", status_code=200)
async def root():
    return "powered by FastAPI"


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "quotable is up and running"


@app.get("/random", status_code=200)
async def get_random_quote():
    random_quote = random.choice(quote_engines)()
    return JSONResponse(random_quote)


@app.post("/random", status_code=200)
async def post_random_quote():
    random_quote = random.choice(quote_engines)()
    return JSONResponse(random_quote)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
