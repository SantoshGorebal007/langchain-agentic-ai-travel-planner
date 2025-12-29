from src.data_loader import load_flights, load_hotels, load_places


def test_load_flights():
    flights = load_flights()
    assert len(flights) > 0
    assert flights[0].price > 0
    assert flights[0].source
    assert flights[0].destination


def test_load_hotels():
    hotels = load_hotels()
    assert len(hotels) > 0
    # assert 0 <= hotels[0].rating <= 5
    assert hotels[0].price_per_night > 0


def test_load_places():
    places = load_places()
    assert len(places) > 0
    assert 0 <= places[0].rating <= 5
    assert places[0].city
