from my_math import add_numbers

def test_add_two_zeros():
    result = add_numbers(0,0)
    assert result == 0 

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5

def test_add_numbers_negative():
    result = add_numbers(-2, 3)
    assert result == 1

# unittest, pytest