# Parametrization

Parametrization is a powerful feature that allows you to run a test with multiple different inputs.

## pytest.mark.parametrize

The `@pytest.mark.parametrize` decorator is the standard way to parametrize a test. You provide the names of the arguments as a string, and a list of tuples with the values.

```python
import pytest

@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9), (10, 10, 20)])
def test_addition(x, y, expected):
    assert x + y == expected
```

## Parametrize with IDs

You can provide custom IDs for your test cases using the `ids` parameter. This makes the test output more readable.

```python
@pytest.mark.parametrize(
    "x, y, expected",
    [(1, 2, 3), (4, 5, 9)],
    ids=["1+2=3", "4+5=9"]
)
def test_addition_with_ids(x, y, expected):
    assert x + y == expected
```

## Indirect Parametrization

Indirect parametrization allows you to apply fixtures to your parametrized values. This is useful when your parameters are resources that need to be set up and torn down.

```python
@pytest.fixture
def my_fixture(request):
    return request.param * 2

@pytest.mark.parametrize("my_fixture", [1, 2, 3], indirect=True)
def test_indirect(my_fixture):
    assert my_fixture in [2, 4, 6]
```
