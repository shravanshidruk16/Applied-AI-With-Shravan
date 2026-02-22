import pytest
from main4 import is_prime

@pytest.mark.parametrize("num , expected",[ # Check the SYNTAX as it is different and complicated
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (17,True),
    (18,False),
    (19,True),
    (25,False),
])

def test_is_prime(num,expected):
    assert is_prime(num) == expected