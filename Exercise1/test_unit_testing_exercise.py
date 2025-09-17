from unit_testing_exercise import (
    sum_of_numbers,
    minimum_number,
    maximum_number,
    average_number,
)


def test_sum_of_numbers():
    assert sum_of_numbers([1, 5, 9]) == 15


def test_minimum_number():
    assert minimum_number([1, 5, 9]) == 1


def test_maximum_number():
    assert maximum_number([1, 5, 9]) == 9


def test_average_number():
    assert average_number([1, 5, 9]) == 5
