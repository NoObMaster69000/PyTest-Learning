# Advanced Fixtures

This section covers some of the most advanced and powerful fixture patterns in pytest.

## Factory as Fixture

A "factory as fixture" is a pattern where a fixture returns a function instead of a value. This allows you to create multiple instances of a resource within a single test, with slight variations.

```python
import pytest

@pytest.fixture
def user_factory():
    def _create_user(name, email):
        return {"name": name, "email": email}
    return _create_user

def test_create_multiple_users(user_factory):
    user1 = user_factory("Alice", "alice@example.com")
    user2 = user_factory("Bob", "bob@example.com")
    assert user1["name"] == "Alice"
    assert user2["name"] == "Bob"
```

## The `request` Object

The `request` object is a special fixture that provides information about the test function that is requesting the fixture. It can be used to access the test's name, markers, and more.

One common use case is to access parameters passed via indirect parametrization.

```python
@pytest.fixture
def my_fixture(request):
    # request.param holds the value from the parametrize decorator
    return request.param * 10

@pytest.mark.parametrize("my_fixture", [1, 2, 3], indirect=True)
def test_request_object(my_fixture):
    assert my_fixture in [10, 20, 30]
```
