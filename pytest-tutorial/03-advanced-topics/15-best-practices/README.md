# Best Practices

This section outlines some of the most important best practices for writing and maintaining a healthy test suite with pytest.

## Test Isolation

Tests should be isolated from each other. The outcome of one test should never depend on the outcome of another.

- **Avoid shared state:** Don't rely on global variables or other shared state between tests.
- **Use fixtures for setup and teardown:** Fixtures are the recommended way to manage the state for your tests, ensuring that each test gets a clean environment.

## The AAA Pattern (Arrange, Act, Assert)

Structure your tests in three distinct parts:

1.  **Arrange:** Set up the initial state for the test. This includes creating objects, preparing data, and setting up mocks.
2.  **Act:** Perform the action that you want to test. This should typically be a single function or method call.
3.  **Assert:** Check that the outcome of the action is what you expected.

```python
def test_addition():
    # Arrange
    a = 5
    b = 10

    # Act
    result = my_math_function(a, b)

    # Assert
    assert result == 15
```

## Clear and Descriptive Naming

- **Test files:** `test_*.py` or `*_test.py`.
- **Test functions:** `test_*`. Use descriptive names that explain what the test is checking (e.g., `test_login_with_invalid_password_raises_error`).
- **Test classes:** `Test*`.

## DRY in Tests (Don't Repeat Yourself)

While the DRY principle is important, be cautious about over-applying it in tests. Sometimes, a little bit of duplication is better than a complex abstraction that makes the tests hard to read.

- **Use helpers and fixtures for common setup and teardown logic.**
- **Avoid complex inheritance hierarchies in your test classes.**

## Test Documentation

- **Docstrings:** Use docstrings to explain the purpose of complex tests.
- **Comments:** Use comments to explain non-obvious parts of a test.

## Handling Flaky Tests

Flaky tests (tests that sometimes pass and sometimes fail) are a major problem in a test suite.

- **Isolate the cause:** Try to identify the source of the flakiness (e.g., race conditions, timing issues, reliance on external services).
- **Use plugins like `pytest-rerunfailures` as a temporary measure, but not as a permanent solution.**
- **Rewrite the test to be more deterministic.**
