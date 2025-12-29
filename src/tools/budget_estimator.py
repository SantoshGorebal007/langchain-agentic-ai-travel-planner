from typing import Dict
from src.data_loader import Flight, Hotel
from src.utils.validators import validate_positive, validate_days


def estimate_budget(
    flight: Flight,
    hotel: Hotel,
    days: int,
    per_day_local_expense: float,
    buffer_percentage: float = 0.1,
) -> Dict:
    """
    Estimate total travel budget with breakdown.

    Args:
        flight (Flight): Selected flight
        hotel (Hotel): Selected hotel
        days (int): Trip duration in days
        per_day_local_expense (float): Food + local transport per day
        buffer_percentage (float): Emergency buffer (default 10%)

    Returns:
        Dict with cost breakdown and total
    """

    validate_days(days)
    validate_positive(per_day_local_expense, "per_day_local_expense")

    flight_cost = flight.price
    hotel_cost = hotel.price_per_night * days
    food_transport_cost = per_day_local_expense * days

    subtotal = flight_cost + hotel_cost + food_transport_cost
    buffer = round(subtotal * buffer_percentage, 2)
    total = round(subtotal + buffer, 2)

    return {
        "flight": round(flight_cost, 2),
        "hotel": round(hotel_cost, 2),
        "food_transport": round(food_transport_cost, 2),
        "buffer": buffer,
        "total": total,
    }
