from unittest.mock import patch
from src.tools.weather_lookup import get_weather


@patch("src.tools.weather_lookup.requests.get")
def test_get_weather_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "daily": {
            "time": ["2025-01-04"],
            "temperature_2m_max": [28.5],
            "temperature_2m_min": [18.2],
            "weathercode": [2]
        }
    }

    result = get_weather(
        lat=28.61,
        lon=77.20,
        start_date="2025-01-04",
        end_date="2025-01-04"
    )

    assert len(result) == 1
    assert result[0]["temp_max"] == 28.5
    assert result[0]["temp_min"] == 18.2


@patch("src.tools.weather_lookup.requests.get")
def test_get_weather_retry_and_fail(mock_get):
    mock_get.side_effect = Exception("API down")

    try:
        get_weather(
            lat=0,
            lon=0,
            start_date="2025-01-01",
            end_date="2025-01-02"
        )
    except RuntimeError as e:
        assert "Weather lookup failed" in str(e)
