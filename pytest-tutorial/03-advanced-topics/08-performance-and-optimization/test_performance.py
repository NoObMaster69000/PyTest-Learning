# test_performance.py
import pytest
import time

# To run the benchmark test, you need the pytest-benchmark plugin:
# pip install pytest-benchmark

def function_to_benchmark(n=1000):
    """A sample function whose performance we want to measure."""
    return sum(range(n))

def test_benchmark_example(benchmark):
    """
    This test uses the `benchmark` fixture from pytest-benchmark.
    The fixture will run the given function multiple times and record the
    timing statistics.
    """
    # The benchmark fixture takes a callable as its first argument.
    # Any additional arguments will be passed to the callable.
    result = benchmark(function_to_benchmark, n=5000)

    # The benchmark will handle the timing and statistics.
    # You can still make assertions about the result of the function.
    assert result == sum(range(5000))

# To demonstrate the --durations flag, here are a couple of slow tests.
@pytest.mark.slow
def test_very_slow():
    """A test that is intentionally slow."""
    time.sleep(0.5)
    assert True

@pytest.mark.slow
def test_moderately_slow():
    """Another test that is intentionally slow, but faster than the first one."""
    time.sleep(0.2)
    assert True

# To see the durations of these tests, run:
# pytest --durations=2 test_performance.py
