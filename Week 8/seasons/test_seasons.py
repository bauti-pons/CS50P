from seasons import number_to_words


def test_conversion():
    assert number_to_words(10897920) == "Ten million, eight hundred ninety-seven thousand, nine hundred twenty minutes"
    assert number_to_words(527040) == "Five hundred twenty-seven thousand forty minutes"
    assert number_to_words(17349120) == "Seventeen million, three hundred forty-nine thousand, one hundred twenty minutes"
    assert number_to_words(-1440) == "Minus one thousand, four hundred forty minutes"
