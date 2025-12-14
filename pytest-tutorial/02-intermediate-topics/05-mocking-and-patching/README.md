# Mocking and Patching

Mocking is a technique for replacing parts of your code with test doubles. This is useful for isolating the code you're testing from its dependencies, such as external services, databases, or complex objects.

## unittest.mock Integration (pytest-mock)

The `pytest-mock` plugin provides a `mocker` fixture that makes it easy to work with Python's built-in `unittest.mock` library.

```python
def test_with_mocker(mocker):
    # Mock a function
    mocker.patch('my_module.my_function', return_value='mocked!')

    # Call the code that uses the function
    result = my_module.some_code()

    # Assert that the result is what we expect
    assert result == 'mocked!'
```

## Monkeypatch Fixture

Pytest also has a built-in `monkeypatch` fixture that can be used for modifying classes, methods, and functions during testing.

```python
def test_with_monkeypatch(monkeypatch):
    # Set an environment variable
    monkeypatch.setenv('MY_VAR', 'my_value')

    # Replace a function
    monkeypatch.setattr(my_module, 'my_function', lambda: 'mocked!')

    # ...
```

The `monkeypatch` fixture is particularly useful for simple modifications, while `mocker` is more powerful and provides more features for complex mocking scenarios.
