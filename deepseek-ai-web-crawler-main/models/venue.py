from pydantic import BaseModel


class Venue(BaseModel):
    """
    Represents the data structure of a Venue.
    """

    category: str
    time: str
    title: str
    description: str
    link: str
