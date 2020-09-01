from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import randint

from quotable.helpers import QuoteData
from quotable.routers.futurama.quotes import futurama_quotes

router = APIRouter()


def generate_quote():
    quote_data: QuoteData = futurama_quotes[randint(0, len(futurama_quotes))]
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
    quote_response = generate_quote()
    return JSONResponse(quote_response)


@router.post("/futurama")
def post_futurama():
    quote_response = generate_quote()
    return JSONResponse(quote_response)
