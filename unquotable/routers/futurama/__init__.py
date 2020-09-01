from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import randint
from typing import List

from unquotable.helpers import QuoteData, QuoteEngine
from unquotable.routers.futurama.quotes import (
    zapp_brannigan_quotes,
    bender_quotes,
    futurama_quotes,
)

router = APIRouter()


class FuturamaQuoteEngine(QuoteEngine):
    def generate_quote(self):
        quote_data: QuoteData = self.quotes[randint(0, len(self.quotes) - 1)]
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
    quote_response = FuturamaQuoteEngine(futurama_quotes).generate_quote()
    return JSONResponse(quote_response)


@router.post("/futurama")
def post_futurama():
    quote_response = FuturamaQuoteEngine(futurama_quotes).generate_quote()
    return JSONResponse(quote_response)


@router.get("/zappbrannigan")
def get_futurama_zappbrannigan():
    quote_response = FuturamaQuoteEngine(zapp_brannigan_quotes).generate_quote()
    return JSONResponse(quote_response)


@router.post("/zappbrannigan")
def post_futurama_zappbrannigan():
    quote_response = FuturamaQuoteEngine(zapp_brannigan_quotes).generate_quote()
    return JSONResponse(quote_response)


@router.get("/bender")
def get_futurama_bender():
    quote_response = FuturamaQuoteEngine(bender_quotes).generate_quote()
    return JSONResponse(quote_response)


@router.post("/bender")
def post_futurama_bender():
    quote_response = FuturamaQuoteEngine(bender_quotes).generate_quote()
    return JSONResponse(quote_response)
