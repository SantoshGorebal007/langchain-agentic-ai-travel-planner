from src.tools.hotel_recommender import recommend_hotels


def test_recommend_hotels_basic():
    results = recommend_hotels(
        city="Delhi",
        checkin="2025-01-04",
        checkout="2025-01-06"
    )
    assert len(results) > 0
    assert results[0].city == "Delhi"


def test_recommend_hotels_price_filter():
    results = recommend_hotels(
        city="Delhi",
        checkin="2025-01-04",
        checkout="2025-01-06",
        max_price=5000
    )
    assert all(h.price_per_night <= 5000 for h in results)


def test_recommend_hotels_rating_filter():
    results = recommend_hotels(
        city="Delhi",
        checkin="2025-01-04",
        checkout="2025-01-06",
        min_rating=4
    )
    assert all(h.stars >= 4 for h in results)
