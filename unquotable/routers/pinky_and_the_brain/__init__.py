from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import randint

from unquotable.helpers import QuoteData
from unquotable.routers.pinky_and_the_brain.quotes import pinky_quotes

router = APIRouter()


def generate_quote():
    quote_data: QuoteData = pinky_quotes[randint(0, 177)]
    quote_response = {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_Pinky, are you pondering what I'm pondering?_ - *Brain*",
                },
            }
        ],
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
                            "text": f"- *{quote_data.person}* _{quote_data.source}_",
                        },
                    },
                ]
            }
        ],
    }

    return quote_response


@router.get("/aypwip")
def get_aypwip():
    quote_response = generate_quote()
    return JSONResponse(quote_response)


@router.post("/aypwip")
def post_aypwip():
    quote_response = generate_quote()
    return JSONResponse(quote_response)
