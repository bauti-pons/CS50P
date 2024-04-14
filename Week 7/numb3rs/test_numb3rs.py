from numb3rs import validate


def test_dot_syntax():
    assert validate("1.2.3.4") == True
    assert validate(".1.2.3.4.") == False
    assert validate("1..2.3.4") == False
    assert validate("1..2..3.4") == False
    assert validate("1..2.3..4") == False
    assert validate("1..2.3.4.") == False


def test_numbers():
    assert validate("0.255.0.255") == True
    assert validate("512.512.512.512") == False
    assert validate("512.0.0.0") == False
    assert validate("0.512.0.0") == False
    assert validate("0.0.0.512") == False


def test_symbols():
    assert validate("€0.255.0.255$") == False
    assert validate("-0.255.0.255-") == False
    assert validate(":0.255.0.255:") == False
    assert validate("º0.255.0.255º") == False



