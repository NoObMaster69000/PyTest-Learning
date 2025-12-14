# test_configuration.py
import pytest

# This test is marked as 'slow'.
# The 'slow' marker is registered in the pytest.ini file.
# You can run all tests except the slow ones with: pytest -m "not slow"
@pytest.mark.slow
def test_slow_operation():
    """
    A test that is marked as slow.
    """
    import time
    time.sleep(1)
    assert True
