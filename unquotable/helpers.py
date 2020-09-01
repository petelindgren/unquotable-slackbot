import logging
from typing import List, NamedTuple, Optional


class QuoteData(NamedTuple):

    quote: str
    person: Optional[str]
    source: Optional[str]

    def from_dict(self, data: dict):
        return QuoteData(
            quote=data.get("quote"),
            person=data.get("person"),
            source=data.get("source"),
        )


class QuoteEngine(object):
    def __init__(self, quotes: List[QuoteData]):
        self.quotes = quotes

    def generate_quote(self):
        raise NotImplementedError
