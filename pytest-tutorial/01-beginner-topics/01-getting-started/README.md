# Getting Started with Pytest

This section covers the basics of getting pytest up and running.

## Installation and Setup

First, you need to install pytest. It's a standard Python package, so you can install it with pip:

```bash
pip install pytest
```

## First Test

Create a file named `test_basic.py`. Pytest will automatically discover this file because it starts with `test_`.

Inside this file, create a function named `test_addition`. Pytest discovers this function because it also starts with `test_`.

```python
# test_basic.py

def test_addition():
    assert 1 + 1 == 2
```

## Running Tests

To run the tests, open your terminal and navigate to the directory containing your test file. Then, simply run the `pytest` command:

```bash
pytest
```

Pytest will discover and run the tests, and you'll see the output indicating that the test passed.
