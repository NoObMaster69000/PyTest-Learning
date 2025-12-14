# Markers

Markers are a way to add metadata to your tests. You can use them to categorize tests, skip tests, or run tests with different parameters.

## Built-in Markers

Pytest provides several built-in markers, such as `@pytest.mark.skip` and `@pytest.mark.skipif`.

```python
import pytest

@pytest.mark.skip(reason="This test is currently broken.")
def test_broken():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_python310_feature():
    # ...
    pass
```

## Parametrize Basics

The `@pytest.mark.parametrize` marker allows you to run a test with multiple sets of inputs.

```python
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

## Custom Markers

You can create your own markers to categorize tests. It's a good practice to register your custom markers in your `pytest.ini` file.

```python
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    smoke: marks tests as smoke tests
```

```python
@pytest.mark.slow
def test_slow_operation():
    # ...
    pass

@pytest.mark.smoke
def test_smoke_test():
    # ...
    pass
```

## Marker Selection

You can run tests based on their markers using the `-m` command-line flag.

```bash
# Run only the smoke tests
pytest -m smoke

# Run all tests except the slow ones
pytest -m "not slow"
```
