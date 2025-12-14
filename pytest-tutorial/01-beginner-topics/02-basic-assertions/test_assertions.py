# test_assertions.py
import pytest

def test_simple_assertions():
    """
    Demonstrates basic assertions for equality, inequality, and boolean checks.
    """
    assert 1 == 1, "1 should be equal to 1"
    assert 1 != 2, "1 should not be equal to 2"
    assert "hello" in "hello world", "'hello' should be in 'hello world'"
    assert True, "This should be True"

def test_exception_raising():
    """
    Tests that a specific exception (ZeroDivisionError) is raised.
    The 'with pytest.raises(...)' block will pass if the expected exception is raised.
    """
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

def test_approximate_comparison():
    """
    Demonstrates the use of pytest.approx() for floating-point comparisons.
    This is necessary because of the inherent imprecision of floating-point arithmetic.
    """
    assert 0.1 + 0.2 == pytest.approx(0.3)
