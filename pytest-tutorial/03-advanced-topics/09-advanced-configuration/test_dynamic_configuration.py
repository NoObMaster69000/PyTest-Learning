# test_dynamic_configuration.py
import pytest

# The 'dynamic_marker' was registered in the conftest.py's pytest_configure hook.
# If you run pytest with --strict-markers, this test will pass because the
# marker has been dynamically registered.
@pytest.mark.dynamic_marker
def test_with_dynamic_marker():
    """
    A test that uses a marker registered dynamically.
    """
    assert True

def test_access_custom_config(custom_message_from_config):
    """
    This test uses a fixture that retrieves a custom message set on the
    config object in pytest_configure.
    """
    assert custom_message_from_config == "Hello from pytest_configure!"

# To demonstrate warning management, let's create a function that
# issues a deprecation warning.
def function_with_deprecation_warning():
    import warnings
    warnings.warn("This function is deprecated.", DeprecationWarning)
    return 42

def test_deprecation_warning():
    """
    This test calls a function that issues a DeprecationWarning.
    By adding `filterwarnings = error` to pytest.ini, you can make this
    test fail.
    """
    assert function_with_deprecation_warning() == 42
