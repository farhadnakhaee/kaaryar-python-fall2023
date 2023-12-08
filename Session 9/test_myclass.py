from my_class import MyClass

def test_multiply():
    obj = MyClass()
    result = obj.multiply(2, 3)
    assert result == 6

def test_multiply_negative():
    obj = MyClass()
    result = obj.multiply(-2, 3)
    assert result == -6

def test_add_two_posive():
    obj = MyClass()
    result = obj.add_numbers(-2, 3)
    assert result == 1