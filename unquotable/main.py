import random

import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from quotable.routers import pinky_and_the_brain
from quotable.routers import futurama
from quotable.routers.futurama import FuturamaQuoteEngine, futurama_quotes

app = FastAPI()
app.include_router(pinky_and_the_brain.router, prefix="")
app.include_router(futurama.router, prefix="")

quote_engines = [
    pinky_and_the_brain.generate_quote,
    FuturamaQuoteEngine(futurama_quotes).generate_quote,
]


@app.get("/", status_code=200)
async def root():
    return "powered by FastAPI"


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "quotable is up and running"


@app.get("/random", status_code=200)
async def get_random_quote():
    quote_engine = random.choice(quote_engines)
    print(f"quote_engines: {quote_engines}")
    try:
        random_quote = quote_engine()
    except TypeError:
        print(f"quote_engine: {quote_engine}")
    return JSONResponse(random_quote)


@app.post("/random", status_code=200)
async def post_random_quote():
    random_quote = random.choice(quote_engines)()
    return JSONResponse(random_quote)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
