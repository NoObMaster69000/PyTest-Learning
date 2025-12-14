# test_advanced_fixtures.py
import pytest

# This fixture depends on the 'base_data' fixture from conftest.py.
# Pytest will automatically resolve the dependency and pass the return
# value of 'base_data' to this fixture.
@pytest.fixture
def user_data(base_data):
    """
    A fixture that builds upon the 'base_data' fixture.
    """
    data = base_data.copy()
    data["email"] = "jules@example.com"
    return data

def test_user_data(user_data):
    """
    This test uses the 'user_data' fixture.
    """
    assert user_data["name"] == "Jules"
    assert user_data["email"] == "jules@example.com"

# This fixture demonstrates setup and teardown using 'yield'.
@pytest.fixture
def temporary_file():
    """
    A fixture that creates a temporary file for a test.
    The 'yield' keyword separates the setup and teardown phases.
    """
    # Setup: create the file
    with open("temp.txt", "w") as f:
        f.write("hello")

    yield "temp.txt"

    # Teardown: remove the file
    import os
    os.remove("temp.txt")

def test_temporary_file(temporary_file):
    """
    This test uses the 'temporary_file' fixture.
    """
    with open(temporary_file, "r") as f:
        content = f.read()
    assert content == "hello"
