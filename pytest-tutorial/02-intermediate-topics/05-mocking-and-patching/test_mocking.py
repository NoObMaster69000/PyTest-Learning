# test_mocking.py
import pytest
from app import get_user_name, get_api_key

def test_get_user_name(mocker):
    """
    Tests the get_user_name function by mocking the requests.get call.
    """
    # Create a mock response object
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"name": "Jules"}

    # Patch the requests.get function to return our mock response
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function we're testing
    user_name = get_user_name(1)

    # Assert that the function returned the correct name
    assert user_name == "Jules"

def test_get_api_key(monkeypatch):
    """
    Tests the get_api_key function by using monkeypatch to set an
    environment variable.
    """
    # Use monkeypatch to set the API_KEY environment variable for this test
    monkeypatch.setenv("API_KEY", "my-secret-key")

    # Call the function and assert that it returns the correct key
    api_key = get_api_key()
    assert api_key == "my-secret-key"
