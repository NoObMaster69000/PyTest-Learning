# test_basic.py

# Pytest discovers test functions based on their names (starting with "test_").
def test_addition():
    """
    A simple test to check the addition operator.
    """
    # The 'assert' keyword is used to check if a condition is true.
    # If the condition is false, the test will fail.
    assert 1 + 1 == 2

def test_subtraction():
    """
    A simple test to check the subtraction operator.
    """
    assert 5 - 3 == 2
