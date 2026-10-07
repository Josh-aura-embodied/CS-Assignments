import pytest


def area_rectangle(length, width):
    return length * width


def test_area_rectangle():
    assert area_rectangle(4, 5) == 20
    assert area_rectangle(2.2, 7.9) == pytest.approx(17.38)


def area_square(side_length):
    return side_length**2


def test_area_square():
    assert area_square(5) == 25
    assert area_square(8.5) == pytest.approx(72.25)


def subtract(a, b):
    return a - b


def test_subtract():
    assert subtract(7, 2) == 5
    assert subtract(7.5, 5.1) == pytest.approx(2.4)
    