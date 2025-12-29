from typing import List, Optional
from src.data_loader import load_hotels, Hotel


def recommend_hotels(
    city: str,
    checkin: str,
    checkout: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    top_n: int = 3,
) -> List[Hotel]:
    """
    Recommend hotels in a city with optional price and rating filters.

    Ranking priority:
    1) Higher stars
    2) Lower price_per_night
    """

    hotels = load_hotels()

    # ---------- Filter ----------
    filtered = [
        h for h in hotels
        if h.city.lower() == city.lower()
    ]

    if max_price is not None:
        filtered = [h for h in filtered if h.price_per_night <= max_price]

    if min_rating is not None:
        filtered = [h for h in filtered if h.stars >= min_rating]

    if not filtered:
        return []

    # ---------- Rank ----------
    # Higher stars first, then lower price
    filtered.sort(key=lambda h: (-h.stars, h.price_per_night))

    return filtered[:top_n]
