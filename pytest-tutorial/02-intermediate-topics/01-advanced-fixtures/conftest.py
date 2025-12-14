# conftest.py
import pytest

# Fixtures defined in a conftest.py file are automatically available to all
# tests in the same directory and its subdirectories.

@pytest.fixture
def base_data():
    """
    A fixture that provides a base dictionary.
    This fixture can be used by other fixtures or tests.
    """
    return {"name": "Jules"}
