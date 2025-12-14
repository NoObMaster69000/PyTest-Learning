# Property-Based Testing

Property-based testing is a powerful technique where you specify the properties or invariants of your code, and the testing framework automatically generates a wide range of inputs to try to falsify those properties.

## `Hypothesis`

The most popular library for property-based testing in Python is `Hypothesis`. It integrates seamlessly with pytest.

**Installation:**
```bash
pip install hypothesis
```

## Writing a Property-Based Test

A property-based test with `Hypothesis` looks like this:

```python
from hypothesis import given
from hypothesis.strategies import text

def my_function_to_test(s):
    # ...
    pass

@given(text())
def test_my_function_property(s):
    # This is a property that should hold true for any string 's'.
    assert len(my_function_to_test(s)) >= len(s)
```

In this example:
- `@given(text())` tells `Hypothesis` to generate arbitrary strings and pass them to the test function.
- `Hypothesis` will run the test many times with different strings, trying to find a case where the assertion fails.

## Key Concepts

- **Strategies:** Strategies are recipes for generating data. `Hypothesis` provides a rich set of built-in strategies (e.g., `integers()`, `floats()`, `lists()`, `dictionaries()`).
- **Shrinking:** When `Hypothesis` finds a failing example, it automatically tries to "shrink" it to the simplest possible failing case. This makes debugging much easier.

Property-based testing is particularly effective for finding edge cases and subtle bugs that are hard to think of when writing example-based tests.
