import pytest

def my_sum(x, y):
    return x + y

def test_my_sum():
    assert my_sum(2,2) == 4