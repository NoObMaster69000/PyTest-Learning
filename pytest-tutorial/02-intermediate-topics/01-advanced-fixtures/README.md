# Advanced Fixtures

This section explores more advanced fixture concepts, including dependencies, factories, and finalization.

## Fixture Dependencies

Fixtures can depend on other fixtures. Just like tests, a fixture can request another fixture by including its name as a parameter.

```python
import pytest

@pytest.fixture
def base_data():
    return {"name": "Jules"}

@pytest.fixture
def user_data(base_data):
    data = base_data.copy()
    data["email"] = "jules@example.com"
    return data
```

## Fixture Finalization (Teardown)

For cleanup logic, you can use `yield` in a fixture. The code after the `yield` statement is the teardown code, which will run after the test has finished.

```python
@pytest.fixture
def db_connection():
    # Setup: create a database connection
    conn = ...
    yield conn
    # Teardown: close the connection
    conn.close()
```

## conftest.py: Sharing Fixtures

Fixtures defined in a `conftest.py` file are automatically discovered by pytest and can be used by any test in the same directory or its subdirectories without needing to be imported. This is the recommended way to share fixtures across your project.
