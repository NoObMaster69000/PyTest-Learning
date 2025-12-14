# test_advanced_fixtures.py
import pytest

# Factory as Fixture: A fixture that returns a function.
# This pattern is useful when you need to create multiple, slightly different
# instances of a resource within a single test.
@pytest.fixture
def user_factory():
    """
    A fixture that returns a factory function for creating user dictionaries.
    """
    def _create_user(name, is_admin=False):
        """The factory function itself."""
        return {"name": name, "is_admin": is_admin}
    return _create_user

def test_user_creation(user_factory):
    """
    This test uses the user_factory to create multiple user objects.
    """
    user1 = user_factory("Alice")
    user2 = user_factory("Bob", is_admin=True)

    assert user1 == {"name": "Alice", "is_admin": False}
    assert user2 == {"name": "Bob", "is_admin": True}


# The `request` object is a special fixture that provides information
# about the test function that is requesting the fixture.
@pytest.fixture
def parameterized_fixture(request):
    """
    This fixture uses the `request.param` attribute to access the value
    passed from the @pytest.mark.parametrize decorator.
    """
    # This demonstrates accessing the parameter.
    # A more complex fixture could use this to set up a specific state.
    return request.param * 10

@pytest.mark.parametrize("parameterized_fixture", [1, 2, 3], indirect=True)
def test_with_request_object(parameterized_fixture):
    """
    This test uses indirect parametrization to pass values to the
    `parameterized_fixture`. The fixture then uses the `request` object
    to access these values.
    """
    assert parameterized_fixture in [10, 20, 30]

# Another example of using the `request` object to inspect the test context.
@pytest.fixture
def inspecting_fixture(request):
    """
    This fixture inspects the requesting test's name and markers.
    """
    return {
        "node_name": request.node.name,
        "markers": [m.name for m in request.node.iter_markers()]
    }

@pytest.mark.smoke
def test_inspected_by_fixture(inspecting_fixture):
    """
    A test that is inspected by the `inspecting_fixture`.
    """
    assert inspecting_fixture["node_name"] == "test_inspected_by_fixture"
    assert "smoke" in inspecting_fixture["markers"]
