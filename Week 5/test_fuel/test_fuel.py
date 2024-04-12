import pytest
from fuel import convert, gauge


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ZeroDivisionError):
        convert("50/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("3/4cat")
    with pytest.raises(ValueError):
        convert("cat3/4")


def test_ints():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("2/3") == 67
    assert convert("1/3") == 33


def test_percentage():
    assert gauge(33) == "33%"
    assert gauge(25) == "25%"
    assert gauge(85) == "85%"
    assert gauge(10) == "10%"


def test_empty_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

