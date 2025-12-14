# Advanced Parametrization

This section explores more advanced ways to use pytest's parametrization features.

## Lazy Parametrization with `pytest.param`

You can use `pytest.param` to apply marks or set IDs for individual parameter sets within a `@pytest.mark.parametrize` call. This is useful for marking specific cases as expected to fail (`xfail`) or for giving them descriptive names.

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        pytest.param(5, 5, 11, marks=pytest.mark.xfail(reason="Incorrect sum")),
        pytest.param(10, 20, 30, id="high_numbers"),
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected
```

## Generating Test Cases Programmatically

Instead of hardcoding the parameter list, you can generate it dynamically. This is useful for creating a large number of test cases from a data source or based on some logic.

```python
def generate_test_data():
    # In a real scenario, this data could come from a file, a database, or an API.
    return [("user", "password"), ("admin", "secret"), ("guest", "guest")]

@pytest.mark.parametrize("username, password", generate_test_data())
def test_login(username, password):
    # Test the login functionality with the generated data.
    assert isinstance(username, str)
    assert isinstance(password, str)
```

## Matrix Testing

You can stack multiple `@pytest.mark.parametrize` decorators to test all possible combinations of the parameters. This is useful for testing functions that have several independent inputs.

```python
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", ["a", "b"])
def test_matrix(x, y):
    # This test will run 4 times with the following combinations:
    # (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
    assert isinstance(x, int)
    assert isinstance(y, str)
```
