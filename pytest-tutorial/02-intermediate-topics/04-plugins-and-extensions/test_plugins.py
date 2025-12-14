# test_plugins.py
import pytest
from my_module import get_data_from_api

# The pytest-mock plugin provides the 'mocker' fixture, which is a wrapper
# around the standard unittest.mock library.

def test_get_data_from_api(mocker):
    """
    This test demonstrates how to use the 'mocker' fixture to mock a function.
    """
    # The mocker.patch() method is used to replace a function with a mock.
    # The first argument is the path to the function to be mocked.
    # The return_value argument specifies what the mock should return when called.
    mocker.patch('my_module.get_data_from_api', return_value='mocked data')

    # Now, when we call the function, it will return the mocked value
    # instead of the real value.
    result = get_data_from_api()

    assert result == 'mocked data'
