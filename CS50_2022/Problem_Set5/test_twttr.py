"""Test"""
from twttr import shorten

def test_default():
    """when no data is entered"""
    assert shorten("") == ""

def test_upper_lower_case():
    """Does it capture uppercase and lowercase letters?"""
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwITtEr") == "TwTtr"

def test_numbers():
    """Does it capture numbers?"""
    assert shorten("1234") == "1234"

def test_punctuation():
    """Does it capture punctuation?"""
    assert shorten("!?,.'") == "!?,.'"
