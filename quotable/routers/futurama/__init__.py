from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import randint
from typing import List

from quotable.helpers import QuoteData
from quotable.routers.futurama.quotes import (
    zapp_brannigan_quotes,
    bender_quotes,
    futurama_quotes,
)

router = APIRouter()


def generate_quote(quote_source: List[QuoteData]):
    quote_data: QuoteData = quote_source[randint(0, len(quote_source))]
    quote_response = {
        "response_type": "in_channel",
        "attachments": [
            {
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"_{quote_data.quote}_"},
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"- *_{quote_data.person}_* {quote_data.source}",
                        },
                    },
                ]
            }
        ],
    }

    return quote_response


@router.get("/futurama")
def get_futurama():
    quote_response = generate_quote(futurama_quotes)
    return JSONResponse(quote_response)


@router.post("/futurama")
def post_futurama():
    quote_response = generate_quote(futurama_quotes)
    return JSONResponse(quote_response)


@router.get("/zapp")
def get_futurama():
    quote_response = generate_quote(zapp_brannigan_quotes)
    return JSONResponse(quote_response)


@router.post("/zapp")
def post_futurama():
    quote_response = generate_quote(zapp_brannigan_quotes)
    return JSONResponse(quote_response)


@router.get("/bender")
def get_futurama():
    quote_response = generate_quote(bender_quotes)
    return JSONResponse(quote_response)


@router.post("/bender")
def post_futurama():
    quote_response = generate_quote(bender_quotes)
    return JSONResponse(quote_response)
