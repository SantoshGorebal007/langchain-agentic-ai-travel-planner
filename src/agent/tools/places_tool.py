from langchain.tools import tool
from pydantic import BaseModel
from typing import List, Optional
from src.tools.places_discovery import discover_places


class PlacesInput(BaseModel):
    city: str
    types: Optional[List[str]] = None
    top_k: int = 10


@tool(args_schema=PlacesInput)
def discover_places_tool(
    city: str,
    types: Optional[List[str]] = None,
    top_k: int = 10,
) -> List[dict]:
    """
    Discover tourist places in a city filtered by type and ranked by rating.
    """
    places = discover_places(
        city=city,
        types=types,
        top_k=top_k,
    )
    return [p.model_dump() for p in places]
