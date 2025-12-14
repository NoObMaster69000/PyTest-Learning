# Plugins and Extensions

Pytest has a rich ecosystem of plugins that extend its functionality. Here are a few of the most popular ones.

## pytest-cov

`pytest-cov` is used for measuring code coverage. It's an essential tool for ensuring your tests are thorough.

**Installation:**
```bash
pip install pytest-cov
```

**Usage:**
```bash
pytest --cov=my_project
```

## pytest-mock

`pytest-mock` provides a `mocker` fixture that makes it easy to use `unittest.mock`.

**Installation:**
```bash
pip install pytest-mock
```

**Usage:**
```python
def test_mocking(mocker):
    # Mock an object or function
    mocker.patch('my_module.my_function', return_value='mocked!')
    # ...
```

## pytest-xdist

`pytest-xdist` allows you to run your tests in parallel, which can significantly speed up your test suite.

**Installation:**
```bash
pip install pytest-xdist
```

**Usage:**
```bash
# Run tests in parallel with auto-detected number of CPUs
pytest -n auto
```
