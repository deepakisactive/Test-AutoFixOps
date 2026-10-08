from app.main import calculate_total


def test_calculate_total():
    assert calculate_total(100, 2) == 250