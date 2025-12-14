# Basic Assertions

Pytest uses the standard `assert` statement for assertions, but it enhances them with "assertion introspection" to provide more detailed feedback on failures.

## Simple Assertions

You can use `assert` to check for equality, inequality, and boolean conditions.

```python
def test_simple_assertions():
    assert 1 == 1
    assert 1 != 2
    assert True
```

## Exception Testing

To check if a function raises an exception, use `pytest.raises()`. The test will pass if the expected exception is raised, and fail otherwise.

```python
import pytest

def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## Approximate Comparisons

For floating-point numbers, use `pytest.approx()` to avoid precision issues.

```python
import pytest

def test_approximate_comparison():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```
