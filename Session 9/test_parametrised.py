import pytest
from my_math import add_numbers

@pytest.mark.parametrize("a, b, expected", 
                         [
                             (1, 2, 3), 
                             (-1, 1, 0), 
                             (0, 0, 0)
                             ]
                         )
def test_add_numbers_parametrized(a, b, expected):
    result = add_numbers(a, b)
    assert result == expected
