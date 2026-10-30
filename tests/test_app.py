
import pytest

from app.main import (
    calculate_total,
    is_valid_quantity,
    calculate_discount,
)


def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        calculate_total(-100, 2)


def test_zero_quantity_is_valid():
    assert is_valid_quantity(0) is True


def test_positive_quantity_is_valid():
    assert is_valid_quantity(2) is True


def test_calculate_discount():
    # A 10% discount on 100 should leave 90.
    assert calculate_discount(100, 10) == 90
