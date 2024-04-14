import pytest
from working import convert


def test_syntax():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9 A M t o 5 P M")
    with pytest.raises(ValueError):
        convert("cat")


def test_values():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 14:00 PM")
    with pytest.raises(ValueError):
        convert("8:750 AM to 4:750 PM")


def test_upper():
    with pytest.raises(ValueError):
        convert("9 AM TO 5 PM")
    with pytest.raises(ValueError):
        convert("9 am to 5 am")
    with pytest.raises(ValueError):
        convert("9 Am To 5 Am")
    with pytest.raises(ValueError):
        convert("9 aM tO 5 aM")


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"





