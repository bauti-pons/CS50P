from plates import is_valid


def test_numChar():
    assert is_valid("a") == False
    assert is_valid("A") == False
    assert is_valid("CSAAA50") == False
    assert is_valid("CS50000") == False


def test_spaces():
    assert is_valid("CS   50") == False
    assert is_valid("C S 5 0") == False


def test_symbols():
    assert is_valid("CS50-") == False
    assert is_valid("-CS50") == False
    assert is_valid("C-S-5-0") == False
    assert is_valid("$&/·") == False


def test_middleNubers():
    assert is_valid("CS50A") == False
    assert is_valid("CS50AA") == False
    assert is_valid("50CS") == False
    assert is_valid("5050") == False

def test_leadingZero():
    assert is_valid("AB012") == False

