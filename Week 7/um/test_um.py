import pytest
from um import count


def test_case():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1


def test_space():
    assert count(" um") == 1
    assert count("um ") == 1
    assert count(" um ") == 1


def test_symbol():
    assert count(", um,") == 1
    assert count(". um.") == 1
    assert count("- um-") == 1


def test_phrase():
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2


