# Specialized Topics

This section provides a brief overview of how pytest can be used for testing in specialized domains.

## Testing Specific Frameworks

Pytest's plugin ecosystem includes powerful extensions for testing popular web frameworks. These plugins provide fixtures and helpers that make it easier to write tests for these frameworks.

- **Django:** `pytest-django`
    - `client` fixture for making requests to your Django application.
    - `admin_client` fixture for testing admin functionality.
    - Automatic database setup and teardown.
- **Flask:** `pytest-flask`
    - `client` fixture for making requests.
    - `live_server` fixture for running a live server for Selenium/Playwright tests.
- **FastAPI:** FastAPI is designed to be easy to test. You typically use the `TestClient` from `starlette.testclient`.

## Testing CLIs

For testing command-line interfaces (CLIs), libraries like `click.testing.CliRunner` or `typer.testing.TyperCliRunner` are commonly used. These tools allow you to invoke your CLI commands from within your tests and make assertions about the output, exit codes, and side effects.

```python
from click.testing import CliRunner
from my_cli import cli

def test_cli_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Jules'])
    assert result.exit_code == 0
    assert 'Hello, Jules!' in result.output
```

## Testing Documentation (doctest)

Python's `doctest` module allows you to write tests in your docstrings. Pytest can discover and run these tests.

To enable doctest integration, use the `--doctest-modules` flag.

```bash
pytest --doctest-modules
```

```python
def my_function(a, b):
    """
    This is a doctest.
    >>> my_function(2, 3)
    5
    """
    return a + b
```
