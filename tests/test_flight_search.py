from src.tools.flight_search import search_flights


def test_search_flights_cheapest():
    results = search_flights(
        src="Hyderabad",
        dst="Delhi",
        date="2025-01-04",
        sort_by="cheapest"
    )

    assert len(results) > 0
    assert results[0].price <= results[-1].price


def test_search_flights_fastest():
    results = search_flights(
        src="Hyderabad",
        dst="Delhi",
        date="2025-01-04",
        sort_by="fastest"
    )

    assert len(results) > 0
    assert results[0].duration_minutes <= results[-1].duration_minutes


def test_search_flights_no_match():
    results = search_flights(
        src="Mumbai",
        dst="Chennai",
        date="2025-01-04"
    )

    assert results == []
