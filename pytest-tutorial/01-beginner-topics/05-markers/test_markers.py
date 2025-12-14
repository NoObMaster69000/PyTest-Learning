# test_markers.py
import pytest
import sys

# The @pytest.mark.skip marker allows you to skip a test.
@pytest.mark.skip(reason="This test is intentionally skipped for demonstration purposes.")
def test_skipped():
    """
    This test will be skipped by pytest.
    """
    assert False

# The @pytest.mark.skipif marker allows you to skip a test based on a condition.
@pytest.mark.skipif(sys.version_info < (3, 10), reason="This test requires Python 3.10 or higher.")
def test_python310_feature():
    """
    This test will be skipped if the Python version is less than 3.10.
    """
    # This is a placeholder for a test that uses a feature from Python 3.10+
    assert True

# The @pytest.mark.parametrize marker allows you to run a test with multiple sets of inputs.
# The first argument is a string of comma-separated parameter names.
# The second argument is a list of tuples, where each tuple contains the values for the parameters.
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2*4", 8), ("6-2", 4)])
def test_eval(test_input, expected):
    """
    This test will be run three times, with different values for 'test_input' and 'expected'.
    """
    assert eval(test_input) == expected

# You can create your own custom markers to categorize tests.
# It's a good practice to register custom markers in your pytest.ini file.
@pytest.mark.smoke
def test_smoke_test():
    """
    This test is marked as a 'smoke' test.
    You can run only the smoke tests with the command: pytest -m smoke
    """
    assert True

@pytest.mark.regression
def test_regression_test():
    """
    This test is marked as a 'regression' test.
    You can run only the regression tests with the command: pytest -m regression
    """
    assert True
