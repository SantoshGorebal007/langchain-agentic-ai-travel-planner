from langchain.tools import tool
from pydantic import BaseModel
from typing import Literal, List
from src.tools.flight_search import search_flights


class FlightSearchInput(BaseModel):
    src: str
    dst: str
    date: str
    sort_by: Literal["cheapest", "fastest"] = "cheapest"


@tool(args_schema=FlightSearchInput)
def search_flights_tool(
    src: str,
    dst: str,
    date: str,
    sort_by: Literal["cheapest", "fastest"] = "cheapest",
) -> List[dict]:
    """
    Search flights between two cities sorted by cheapest or fastest.
    """
    flights = search_flights(
        src=src,
        dst=dst,
        date=date,
        sort_by=sort_by,
    )

    return [f.model_dump() for f in flights]
