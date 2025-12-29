from typing import List, Literal
from src.data_loader import load_flights, Flight


SortType = Literal["cheapest", "fastest"]


def search_flights(
    src: str,
    dst: str,
    date: str,
    sort_by: SortType = "cheapest",
    top_n: int = 3,
) -> List[Flight]:
    """
    Search flights by source and destination.

    Args:
        src (str): Source city
        dst (str): Destination city
        date (str): Travel date (YYYY-MM-DD) [currently informational]
        sort_by (str): 'cheapest' or 'fastest'
        top_n (int): Number of flights to return

    Returns:
        List[Flight]: Filtered and sorted flight options
    """

    flights = load_flights()

    # ---------- Filter ----------
    filtered = [
        f for f in flights
        if f.source.lower() == src.lower()
        and f.destination.lower() == dst.lower()
    ]

    if not filtered:
        return []

    # ---------- Sort ----------
    if sort_by == "cheapest":
        filtered.sort(key=lambda f: f.price)
    elif sort_by == "fastest":
        filtered.sort(key=lambda f: f.duration_minutes)
    else:
        raise ValueError("sort_by must be 'cheapest' or 'fastest'")

    return filtered[:top_n]
