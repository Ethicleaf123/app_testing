from src.math_operations import add, subtract

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_sub():
    assert sub(10, 5) == 5
    assert sub(5, 10) == -5
    assert sub(4, 3) == 1
    assert sub(2, 3) == -1