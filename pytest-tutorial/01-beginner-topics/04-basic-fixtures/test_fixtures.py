# test_fixtures.py
import pytest

# A fixture is a function that provides a fixed baseline for tests.
# You define a fixture by decorating a function with @pytest.fixture.
@pytest.fixture
def sample_data():
    """
    A simple fixture that returns a dictionary.
    This fixture has 'function' scope by default, meaning it's created
    once for each test function that uses it.
    """
    return {"name": "Jules", "email": "jules@example.com"}

# To use a fixture, you include its name as a parameter in your test function.
def test_name(sample_data):
    """
    This test uses the 'sample_data' fixture.
    Pytest will automatically call the fixture and pass its return value
    to the test function.
    """
    assert sample_data["name"] == "Jules"

def test_email(sample_data):
    """
    This test also uses the 'sample_data' fixture.
    A new instance of the fixture is created for this test.
    """
    assert sample_data["email"] == "jules@example.com"

# Fixtures can also be used for setup and teardown.
# The 'yield' keyword separates the setup code from the teardown code.
@pytest.fixture(scope="module")
def module_scoped_fixture():
    """
    A module-scoped fixture is created once per module.
    This is useful for expensive setup and teardown operations.
    """
    print("\\nSetting up module-scoped fixture")
    yield
    print("\\nTearing down module-scoped fixture")

def test_with_module_scoped_fixture(module_scoped_fixture):
    """
    This test uses the module-scoped fixture.
    """
    assert True
