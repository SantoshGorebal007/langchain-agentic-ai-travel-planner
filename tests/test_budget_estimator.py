from src.tools.budget_estimator import estimate_budget
from src.data_loader import load_flights, load_hotels


def test_estimate_budget_basic():
    flight = load_flights()[0]
    hotel = load_hotels()[0]

    result = estimate_budget(
        flight=flight,
        hotel=hotel,
        days=3,
        per_day_local_expense=1000
    )

    assert result["flight"] == flight.price
    assert result["hotel"] == hotel.price_per_night * 3
    assert result["food_transport"] == 3000
    assert result["total"] > 0


def test_estimate_budget_invalid_days():
    flight = load_flights()[0]
    hotel = load_hotels()[0]

    try:
        estimate_budget(
            flight=flight,
            hotel=hotel,
            days=0,
            per_day_local_expense=500
        )
    except ValueError as e:
        assert "days" in str(e).lower()
