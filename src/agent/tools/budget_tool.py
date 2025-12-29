from langchain.tools import tool
from pydantic import BaseModel
from src.tools.budget_estimator import estimate_budget
from src.data_loader import load_flights, load_hotels


class BudgetInput(BaseModel):
    days: int
    per_day_local_expense: float


@tool(args_schema=BudgetInput)
def estimate_budget_tool(
    days: int,
    per_day_local_expense: float,
) -> dict:
    """
    Estimate total travel budget with breakdown (flight, hotel, food/transport, buffer).
    """
    # For now, select the first available flight and hotel
    flight = load_flights()[0]
    hotel = load_hotels()[0]

    return estimate_budget(
        flight=flight,
        hotel=hotel,
        days=days,
        per_day_local_expense=per_day_local_expense,
    )
