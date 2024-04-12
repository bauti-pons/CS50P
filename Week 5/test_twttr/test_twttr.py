from twttr import shorten


def test_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("AeIoU") == ""
    assert shorten("aEiOu") == ""


def test_symbols():
    assert shorten("!·$%&()") == "!·$%&()"
    assert shorten("?¿`+*^-_¨Ç<>") == "?¿`+*^-_¨Ç<>"


def test_numers():
    assert shorten("Hello 123") == "Hll 123"
    assert shorten("0123456789") == "0123456789"
