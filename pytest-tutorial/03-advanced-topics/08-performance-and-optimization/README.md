# Performance and Optimization

As your test suite grows, performance can become a significant issue. A slow test suite can hinder development velocity. This section covers tools and techniques for speeding up your tests.

## `pytest-xdist`

As mentioned in the intermediate topics, `pytest-xdist` is the primary tool for parallelizing your tests.

```bash
# Run tests in parallel, automatically detecting the number of CPUs
pytest -n auto
```

## Test Selection Strategies

Running only the tests that are relevant to your changes can save a lot of time.

- `--lf` (`--last-failed`): Run only the tests that failed on the last run.
- `--ff` (`--failed-first`): Run all tests, but run the ones that failed last time first.

## `pytest-benchmark`

For micro-benchmarking, the `pytest-benchmark` plugin is an excellent tool. It provides a `benchmark` fixture that you can use to measure the performance of your code.

**Installation:**
```bash
pip install pytest-benchmark
```

**Usage:**
```python
def my_function_to_benchmark():
    # ... some code ...
    pass

def test_my_function_performance(benchmark):
    benchmark(my_function_to_benchmark)
```

## Profiling Slow Tests

To identify slow tests, you can use the `--durations` option. This will show you the slowest N tests.

```bash
# Show the 10 slowest tests
pytest --durations=10
```

Once you've identified a slow test, you can use a profiler like `cProfile` to understand where it's spending its time.
