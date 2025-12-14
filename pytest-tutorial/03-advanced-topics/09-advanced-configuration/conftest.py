# conftest.py
import pytest

def pytest_configure(config):
    """
    This hook is called after the command-line options have been parsed.
    It allows for programmatic configuration.
    """
    # 1. Add a custom marker dynamically.
    # This is useful for plugins that want to add markers without requiring
    # the user to add them to their pytest.ini.
    config.addinivalue_line(
        "markers", "dynamic_marker: A marker added dynamically in pytest_configure."
    )

    # 2. Set a custom attribute on the config object.
    # This can be used to share global state or configuration with fixtures and tests.
    config.custom_message = "Hello from pytest_configure!"

@pytest.fixture
def custom_message_from_config(request):
    """
    A fixture that retrieves the custom message from the config object.
    """
    return request.config.custom_message
