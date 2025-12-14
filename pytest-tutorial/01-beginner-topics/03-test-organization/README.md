# Test Organization

Organizing your tests is crucial for maintaining a healthy and scalable test suite. Pytest offers several ways to structure your tests.

## Test Files and Modules

Pytest discovers tests in files named `test_*.py` or `*_test.py`. Each file is a Python module, and you can organize your tests by grouping related tests into the same file.

## Test Classes

You can group related tests into classes. This is a good way to share setup and teardown logic (which we'll cover later with fixtures).

```python
class TestMyClass:
    def test_my_method(self):
        assert 1 == 1

    def test_another_method(self):
        assert "a" in "abc"
```

## Test Functions

For simple tests, you can use standalone functions.

```python
def test_standalone_function():
    assert True
```
