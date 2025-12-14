# Custom Plugins

Pytest's functionality can be extended by writing custom plugins. The simplest way to create a plugin is by using hook functions in a `conftest.py` file.

## Hook Functions

Hook functions are special functions that pytest calls at different points during its execution. By implementing these hooks in your `conftest.py`, you can modify pytest's behavior.

## `conftest.py` Hooks

Placing hook implementations in a `conftest.py` file makes them available to all tests in that directory and its subdirectories. This is a great way to add project-specific customizations.

### Common Hooks

- `pytest_addoption`: Adds a custom command-line option.
- `pytest_configure`: Called after command-line options are parsed. Useful for setting up global state.
- `pytest_collection_modifyitems`: Allows you to modify the list of collected test items. You can use this to reorder tests, filter them, or add custom markers.

Here's an example of how to add a command-line option to specify an environment (e.g., "dev", "staging", "prod"):

```python
# conftest.py

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
```

You can then use the `env` fixture in your tests to get the value of the command-line option.

```python
def test_environment(env):
    if env == "prod":
        # Run tests for production environment
        ...
    elif env == "staging":
        # Run tests for staging environment
        ...
```
