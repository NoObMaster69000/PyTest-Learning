# Configuration

Pytest can be configured in several ways, with `pytest.ini` being the most common.

## pytest.ini

The `pytest.ini` file is the primary configuration file for pytest. It should be placed in the root directory of your project.

Here's an example of a `pytest.ini` file:

```ini
[pytest]
# Add default command-line options
addopts = -ra -q

# Set the paths to search for tests
testpaths = tests

# Register custom markers
markers =
    slow: marks tests as slow
    smoke: marks tests as smoke tests
```

## pyproject.toml

Modern Python projects often use `pyproject.toml` for configuration. Pytest can also be configured in this file.

```toml
[tool.pytest.ini_options]
addopts = "-ra -q"
testpaths = [
    "tests",
]
markers = [
    "slow: marks tests as slow",
    "smoke: marks tests as smoke tests",
]
```

## setup.cfg

`setup.cfg` is another option for configuration, particularly in older projects.

```ini
[tool:pytest]
addopts = -ra -q
testpaths = tests
markers =
    slow
    smoke
```
