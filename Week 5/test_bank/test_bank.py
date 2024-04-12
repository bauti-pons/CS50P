from bank import value


def test_lower():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HeLLo") == 0
    assert value("hEllO") == 0

def test_numbers():
    assert value("0Hello") == 100
    assert value("1hello") == 100
    assert value("5Hi") == 100
    assert value("7hi") == 100

def test_symbols():
    assert value(".Hello") == 100
    assert value("_hello") == 100
    assert value("*Hi") == 100
    assert value("&hi") == 100

def test_h():
    assert value("H") == 20
    assert value("h") == 20
    assert value("Hi darlin") == 20
    assert value("hi darlin") == 20

