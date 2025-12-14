# Basic Fixtures

Fixtures are a powerful feature of pytest that provide a fixed baseline for tests. They are functions that can be used for setup, teardown, and providing data to tests.

## Fixture Basics

You create a fixture by decorating a function with `@pytest.fixture`.

```python
import pytest

@pytest.fixture
def my_data():
    return {"name": "Jules", "age": 30}
```

## Using Fixtures

Tests can "request" a fixture by including its name as a function parameter.

```python
def test_my_data(my_data):
    assert my_data["name"] == "Jules"
```

## Fixture Scopes

Fixtures can have different "scopes," which control how often they are created and destroyed. The available scopes are `function` (the default), `class`, `module`, and `session`.

```python
@pytest.fixture(scope="module")
def module_scoped_fixture():
    print("Setting up module-scoped fixture")
    yield
    print("Tearing down module-scoped fixture")
```
