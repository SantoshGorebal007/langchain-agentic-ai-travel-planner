from src.tools.places_discovery import discover_places


def test_discover_places_basic():
    results = discover_places(city="Delhi")
    assert len(results) > 0
    assert results[0].city == "Delhi"


def test_discover_places_type_filter():
    results = discover_places(
        city="Delhi",
        types=["lake"]
    )
    assert len(results) > 0
    assert all(p.type == "lake" for p in results)


def test_discover_places_ranking():
    results = discover_places(city="Delhi")
    assert results[0].rating >= results[-1].rating
