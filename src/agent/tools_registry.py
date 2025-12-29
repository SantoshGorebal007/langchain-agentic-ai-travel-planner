from src.agent.tools.flight_tool import search_flights_tool
from src.agent.tools.hotel_tool import recommend_hotels_tool
from src.agent.tools.places_tool import discover_places_tool
from src.agent.tools.weather_tool import get_weather_tool
from src.agent.tools.budget_tool import estimate_budget_tool


def get_all_tools():
    return [
        search_flights_tool,
        recommend_hotels_tool,
        discover_places_tool,
        get_weather_tool,
        estimate_budget_tool,
    ]
