# Integration Testing

Integration testing is the phase in software testing in which individual software modules are combined and tested as a group. Pytest is an excellent tool for writing integration tests, especially when combined with fixtures for managing external resources like databases and APIs.

## Database Testing

Fixtures are the key to managing database connections and transactions in your tests. A common pattern is to have a session-scoped fixture that sets up the database, and a function-scoped fixture that manages transactions for each test.

```python
import pytest

@pytest.fixture(scope="session")
def db_engine():
    # Create a database engine
    engine = create_engine("sqlite:///:memory:")
    # Create tables
    Base.metadata.create_all(engine)
    yield engine

@pytest.fixture
def db_session(db_engine):
    # Create a new session for each test
    with Session(db_engine) as session:
        yield session
        # Rollback the transaction after the test
        session.rollback()
```

This pattern ensures that each test runs in a clean, isolated transaction.

## API Testing

When testing code that interacts with external APIs, it's a good practice to use a library like `requests` or `httpx`. For the tests themselves, you can either mock the API calls (as covered in the mocking sections) or test against a real, non-production instance of the API.

Pytest fixtures can be used to manage API clients, authentication tokens, and other resources.

## File System Testing (`tmp_path`)

Pytest provides a built-in `tmp_path` fixture that creates a temporary directory for your tests. This is extremely useful for tests that need to read or write files.

```python
def test_write_to_file(tmp_path):
    # tmp_path is a pathlib.Path object
    file_path = tmp_path / "my_file.txt"
    file_path.write_text("hello world")
    assert file_path.read_text() == "hello world"
```
