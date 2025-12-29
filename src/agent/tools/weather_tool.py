from langchain.tools import tool
from pydantic import BaseModel
from typing import List, Dict
from src.tools.weather_lookup import get_weather


class WeatherInput(BaseModel):
    lat: float
    lon: float
    start_date: str
    end_date: str


@tool(args_schema=WeatherInput)
def get_weather_tool(
    lat: float,
    lon: float,
    start_date: str,
    end_date: str,
) -> List[Dict]:
    """
    Get daily weather forecast (max/min temperature and weather code).
    """
    return get_weather(
        lat=lat,
        lon=lon,
        start_date=start_date,
        end_date=end_date,
    )
