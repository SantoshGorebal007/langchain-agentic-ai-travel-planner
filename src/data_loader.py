import json
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


# =====================
# Pydantic Models (Canonical)
# =====================

class Flight(BaseModel):
    flight_id: str
    airline: str
    source: str
    destination: str
    departure_time: str
    arrival_time: str
    duration_minutes: int
    price: float


class Hotel(BaseModel):
    hotel_id: str
    name: str
    city: str
    stars: int
    price_per_night: float
    amenities: List[str]


class Place(BaseModel):
    place_id: str
    name: str
    city: str
    type: str
    rating: float


# =====================
# Path
# =====================

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


# =====================
# Helpers
# =====================

def _calculate_duration(dep: str, arr: str) -> int:
    """Return duration in minutes."""
    dep_dt = datetime.fromisoformat(dep)
    arr_dt = datetime.fromisoformat(arr)
    return int((arr_dt - dep_dt).total_seconds() // 60)


# =====================
# Normalizers
# =====================

def _normalize_flight(item: dict) -> dict:
    duration = _calculate_duration(
        item["departure_time"],
        item["arrival_time"]
    )

    return {
        "flight_id": item["flight_id"],
        "airline": item["airline"],
        "source": item["from"],
        "destination": item["to"],
        "departure_time": item["departure_time"],
        "arrival_time": item["arrival_time"],
        "duration_minutes": duration,
        "price": item["price"],
    }


def _normalize_hotel(item: dict) -> dict:
    return {
        "hotel_id": item["hotel_id"],
        "name": item["name"],
        "city": item["city"],
        "stars": item["stars"],
        "price_per_night": item["price_per_night"],
        "amenities": item.get("amenities", []),
    }


def _normalize_place(item: dict) -> dict:
    return {
        "place_id": item["place_id"],
        "name": item["name"],
        "city": item["city"],
        "type": item["type"],
        "rating": item["rating"],
    }


# =====================
# Loaders
# =====================

def load_flights() -> List[Flight]:
    with open(DATA_DIR / "flights.json", encoding="utf-8") as f:
        raw = json.load(f)
    return [Flight(**_normalize_flight(item)) for item in raw]


def load_hotels() -> List[Hotel]:
    with open(DATA_DIR / "hotels.json", encoding="utf-8") as f:
        raw = json.load(f)
    return [Hotel(**_normalize_hotel(item)) for item in raw]


def load_places() -> List[Place]:
    with open(DATA_DIR / "places.json", encoding="utf-8") as f:
        raw = json.load(f)
    return [Place(**_normalize_place(item)) for item in raw]
