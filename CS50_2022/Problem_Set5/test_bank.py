"""Test"""
from bank import value

def test_0():
    """Testing return 0"""
    assert value("hello") == "$0"
    assert value("Hello, Evrim") == "$0"
    assert value("HeLLo") == "$0"

def test_20():
    """Testing return 20"""
    assert value("hey") == "$20"
    assert value("hi") == "$20"

def test_100():
    """Testing return 100"""
    assert value("Gunaydin") == "$100"
    assert value("Wsp!") == "$100"
