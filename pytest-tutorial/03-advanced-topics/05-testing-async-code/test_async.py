# test_async.py
import asyncio
import pytest

# To run these tests, you need the pytest-asyncio plugin:
# pip install pytest-asyncio

# The @pytest.mark.asyncio decorator tells pytest to run this test
# function using an asyncio event loop.
@pytest.mark.asyncio
async def test_simple_async_function():
    """
    A simple async test function.
    """
    # The `await` keyword is used to pause the function until the
    # asynchronous operation (in this case, asyncio.sleep) is complete.
    await asyncio.sleep(0.01)
    assert True

# An example of a simple async function that we might want to test.
async def fetch_data():
    """An example async function that simulates a network request."""
    await asyncio.sleep(0.01)
    return {"data": "some data"}

@pytest.mark.asyncio
async def test_fetch_data():
    """
    Tests the fetch_data async function.
    """
    result = await fetch_data()
    assert result == {"data": "some data"}

# You can also create async fixtures.
# These are useful for setting up and tearing down resources that have an async API.
@pytest.fixture
async def async_database_connection():
    """
    An async fixture that simulates connecting to and disconnecting from a database.
    """
    print("\\nConnecting to the async database...")
    await asyncio.sleep(0.01) # Simulate async connection

    yield {"db": "my_async_db"}

    print("\\nDisconnecting from the async database...")
    await asyncio.sleep(0.01) # Simulate async disconnection

@pytest.mark.asyncio
async def test_with_async_fixture(async_database_connection):
    """
    This test uses the async_database_connection fixture.
    The test will not run until the async setup of the fixture is complete.
    """
    assert async_database_connection["db"] == "my_async_db"
