# Advanced Mocking

While `pytest-mock` and `monkeypatch` cover most use cases, `unittest.mock` provides more advanced features for complex mocking scenarios.

## `MagicMock`

`MagicMock` is a subclass of `Mock` that has default implementations of most magic methods (e.g., `__str__`, `__int__`). This is useful when you need to mock objects that are used in operations like arithmetic or comparisons.

```python
from unittest.mock import MagicMock

mock = MagicMock()
mock.__int__.return_value = 100
int(mock)  # returns 100
```

## Mocking Properties with `PropertyMock`

You can use `PropertyMock` to mock properties on objects. This allows you to control the value that is returned when the property is accessed.

```python
from unittest.mock import PropertyMock

class MyClass:
    @property
    def my_property(self):
        return "real value"

mocker.patch(__name__ + '.MyClass.my_property', new_callable=PropertyMock, return_value='mocked value')
instance = MyClass()
assert instance.my_property == 'mocked value'
```

## Verifying Mock Calls

Mocks record how they are called. You can use this to make assertions about how your code is interacting with its dependencies.

- `mock.assert_called()`: Asserts that the mock was called at least once.
- `mock.assert_called_once()`: Asserts that the mock was called exactly once.
- `mock.assert_called_with(*args, **kwargs)`: Asserts that the last call to the mock was with the specified arguments.
- `mock.assert_any_call(*args, **kwargs)`: Asserts that the mock was called at least once with the specified arguments.
- `mock.call_args`: A tuple of the arguments from the last call.
- `mock.call_args_list`: A list of all calls made to the mock.

```python
mock_function = mocker.patch('my_module.my_function')
my_module.call_the_function(1, 2)
mock_function.assert_called_once_with(1, 2)
```
