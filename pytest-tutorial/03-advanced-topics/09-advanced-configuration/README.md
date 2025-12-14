# Advanced Configuration

This section covers more advanced configuration topics, including dynamic configuration and customizing test collection.

## Dynamic Configuration with `pytest_configure`

The `pytest_configure` hook is called after the command-line options have been parsed. It allows you to programmatically modify the configuration. This is useful for setting up global state, registering markers dynamically, or interacting with other plugins.

```python
# conftest.py

def pytest_configure(config):
    # Set a global variable that can be accessed by tests.
    config.my_global_variable = "hello world"

    # Register a custom marker dynamically.
    config.addinivalue_line(
        "markers", "dynamic_marker: a marker added from pytest_configure"
    )
```

## Customizing Test Collection

You can customize how pytest discovers tests by creating your own test collectors. This is an advanced feature that allows you to integrate pytest with other testing frameworks or to define your own conventions for test discovery.

This is typically done by implementing the `pytest_collect_file` hook in a plugin or `conftest.py`.

```python
# conftest.py

def pytest_collect_file(parent, path):
    if path.ext == ".yaml" and path.basename.startswith("test_"):
        # This tells pytest to use our custom collector for YAML files
        # that start with "test_".
        return YamlFile.from_parent(parent, fspath=path)

class YamlFile(pytest.File):
    def collect(self):
        # This method is responsible for parsing the file and yielding
        # test items.
        # ...
        pass
```

## Warning Management

Pytest can be configured to treat warnings as errors, which is a good practice for maintaining a clean codebase. You can use the `filterwarnings` option in your `pytest.ini` to control how warnings are handled.

```ini
# pytest.ini
[pytest]
filterwarnings =
    error
    # Ignore deprecation warnings from a specific library
    ignore::DeprecationWarning:some_library.*
```
