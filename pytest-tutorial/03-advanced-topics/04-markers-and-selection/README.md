# Markers and Selection

This section covers advanced techniques for selecting and working with markers.

## Complex Marker Expressions

You can use boolean logic with the `-m` flag to create complex expressions for selecting tests.

```bash
# Run tests that are marked with 'smoke' AND 'regression'
pytest -m "smoke and regression"

# Run tests that are marked with 'smoke' OR 'regression'
pytest -m "smoke or regression"

# Run tests that are NOT marked with 'slow'
pytest -m "not slow"
```

## Keyword Selection

The `-k` flag allows you to select tests based on keywords in their names.

```bash
# Run tests with 'login' in their name
pytest -k "login"

# Run tests with 'user' but not 'guest' in their name
pytest -k "user and not guest"
```

## Node IDs

Every test has a unique `nodeid`, which includes the file path, class name (if any), and function name. You can run a specific test by providing its `nodeid`.

```bash
# Run a specific test function in a file
pytest tests/test_auth.py::test_login_valid_user

# Run all tests in a specific class
pytest tests/test_auth.py::TestLogin
```
