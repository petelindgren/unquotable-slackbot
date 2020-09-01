from typing import NamedTuple, Optional


class QuoteData(NamedTuple):

    quote: str
    person: Optional[str]

    def from_dict(self, data: dict):
        return QuoteData(quote=data.get("quote"), person=data.get("person"))
