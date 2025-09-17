import pytest
from unit_testing1 import division


def test_positive_numbers():
    assert division(4, 2) == 2


def test_negative_numbers():
    assert division(-8, -2) == 4


def test_bigger_denominator():
    assert division(2, 4) == 0.5


def test_dividing_by_zero():
    with pytest.raises(ValueError):
        division(7, 0)


def test_zero_numerator():
    assert division(0, 9) == 0
