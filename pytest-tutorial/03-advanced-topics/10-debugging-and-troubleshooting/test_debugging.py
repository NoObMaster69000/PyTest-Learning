# test_debugging.py
import logging

# Set up a logger for this module.
logger = logging.getLogger(__name__)

def function_with_a_bug(x):
    """A simple function with a bug."""
    return x / 0

def test_that_fails():
    """
    This test is designed to fail. You can use it to experiment with
    pytest's debugging features.

    Try running this test with the following commands:
    - pytest test_debugging.py --pdb
    - pytest test_debugging.py --tb=long
    """
    result = function_with_a_bug(5)
    assert result == 5

def test_with_print_statements():
    """
    This test uses print() for debugging. To see the output, you need
    to run pytest with the -s flag:

    pytest -s test_debugging.py
    """
    print("\\n--- Inside the test ---")
    x = 10
    print(f"The value of x is {x}")
    assert x == 10

def test_with_logging():
    """
    This test uses the logging module. To see the log messages, you
    need to set the log level:

    pytest --log-cli-level=INFO test_debugging.py
    """
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    assert True
