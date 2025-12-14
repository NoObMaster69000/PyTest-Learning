# test_custom_plugins.py
import pytest

# This test uses the 'env' fixture defined in the conftest.py file.
# The value of 'env' will be determined by the --env command-line option.
# For example, to run this test with the 'staging' environment:
# pytest --env=staging

def test_environment_specific_behavior(env):
    """
    This test demonstrates how to use a custom fixture to run different
    code based on the environment.
    """
    if env == "dev":
        print("Running tests in the development environment.")
        assert True
    elif env == "staging":
        print("Running tests in the staging environment.")
        assert True
    elif env == "prod":
        print("Running tests in the production environment.")
        # This is where you might have production-specific assertions.
        assert True
    else:
        pytest.fail(f"Unknown environment: {env}")

# This test is marked as 'slow'. The `pytest_collection_modifyitems` hook in
# conftest.py will detect this marker and add a 'timeout' marker to the test.
@pytest.mark.slow
def test_slow_operation_with_custom_marker():
    """
    A test that is marked as slow. The custom plugin in conftest.py
    will automatically apply a timeout to this test.
    """
    import time
    time.sleep(1) # This should be well within the 30s timeout.
    assert True
