import time
import requests
from typing import Dict, List


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
MAX_RETRIES = 3
TIMEOUT = 10  # seconds


def get_weather(
    lat: float,
    lon: float,
    start_date: str,
    end_date: str,
) -> List[Dict]:
    """
    Fetch daily weather forecast from Open-Meteo.

    Returns:
        List of dicts with:
        - date
        - temp_max
        - temp_min
        - weather_code
    """

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "weathercode"
        ],
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "auto"
    }

    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(
                OPEN_METEO_URL,
                params=params,
                timeout=TIMEOUT
            )
            response.raise_for_status()

            data = response.json()
            daily = data.get("daily")

            if not daily:
                raise ValueError("No daily weather data returned")

            result = []
            for i in range(len(daily["time"])):
                result.append({
                    "date": daily["time"][i],
                    "temp_max": daily["temperature_2m_max"][i],
                    "temp_min": daily["temperature_2m_min"][i],
                    "weather_code": daily["weathercode"][i],
                })

            return result

        except Exception as e:
            last_error = e
            time.sleep(1)  # backoff

    raise RuntimeError(f"Weather lookup failed after {MAX_RETRIES} retries: {last_error}")
