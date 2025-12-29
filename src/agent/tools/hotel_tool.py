from langchain.tools import tool
from pydantic import BaseModel
from typing import Optional, List
from src.tools.hotel_recommender import recommend_hotels


class HotelInput(BaseModel):
    city: str
    checkin: str
    checkout: str
    max_price: Optional[float] = None
    min_rating: Optional[int] = None


@tool(args_schema=HotelInput)
def recommend_hotels_tool(
    city: str,
    checkin: str,
    checkout: str,
    max_price: Optional[float] = None,
    min_rating: Optional[int] = None,
) -> List[dict]:
    """
    Recommend hotels in a city based on price and rating.
    """
    hotels = recommend_hotels(
        city=city,
        checkin=checkin,
        checkout=checkout,
        max_price=max_price,
        min_rating=min_rating,
    )
    return [h.model_dump() for h in hotels]
