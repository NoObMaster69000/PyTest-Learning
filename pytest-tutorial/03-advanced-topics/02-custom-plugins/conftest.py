# conftest.py
import pytest

# This conftest.py demonstrates some common pytest hook functions.

# `pytest_addoption` is a hook for adding custom command-line options.
def pytest_addoption(parser):
    """
    Adds the --env command-line option to pytest.
    """
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="The environment to run tests against (e.g., dev, staging, prod)."
    )

# A fixture can be used to retrieve the value of the custom command-line option.
@pytest.fixture(scope="session")
def env(request):
    """
    A session-scoped fixture that returns the value of the --env option.
    """
    return request.config.getoption("--env")

# `pytest_collection_modifyitems` is a hook for modifying the list of collected tests.
def pytest_collection_modifyitems(config, items):
    """
    This hook is called after test collection. It can be used to reorder,
    filter, or modify the collected tests.
    """
    # Example: If a test is marked with 'slow', we can add a custom marker to it.
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(pytest.mark.timeout(30))
