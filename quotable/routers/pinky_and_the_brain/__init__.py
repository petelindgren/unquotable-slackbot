from fastapi import APIRouter
from fastapi.responses import JSONResponse
from random import randint

from quotable.helpers import QuoteData
from quotable.routers.pinky_and_the_brain.quotes import pinky_quotes

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
                    "text": "_Pinky, are you pondering what I'm pondering?_\n- *Brain*",
                },
            }
        ],
        "attachments": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"_{quote_data.quote}_"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"- *_{quote_data.person}_*"},
            },
        ],
    }

    return quote_response


@router.get("/aypwip")
def aypwip():
    quote_response = generate_quote()
    return JSONResponse(quote_response)


@router.post("/aypwip")
def aypwip():
    quote_response = generate_quote()
    return JSONResponse(quote_response)
