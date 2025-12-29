from typing import List
from src.data_loader import load_places, Place


def discover_places(
    city: str,
    types: List[str] | None = None,
    top_k: int = 10,
) -> List[Place]:
    """
    Discover places in a city filtered by types and ranked by rating.
    """

    places = load_places()

    filtered = [
        p for p in places
        if p.city.lower() == city.lower()
    ]

    if types:
        types_lower = {t.lower() for t in types}
        filtered = [
            p for p in filtered
            if p.type.lower() in types_lower
        ]

    if not filtered:
        return []

    # Rank by rating (highest first)
    filtered.sort(key=lambda p: p.rating, reverse=True)

    return filtered[:top_k]
