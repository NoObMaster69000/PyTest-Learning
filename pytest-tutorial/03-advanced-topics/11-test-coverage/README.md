# Test Coverage

Test coverage is a metric that measures how much of your code is executed by your tests. It's a useful tool for identifying parts of your codebase that are not well-tested.

## `pytest-cov`

The `pytest-cov` plugin is the standard tool for measuring code coverage with pytest.

**Installation:**
```bash
pip install pytest-cov
```

## Usage

To generate a coverage report, use the `--cov` flag. You can specify the package or module you want to measure coverage for.

```bash
# Measure coverage for the 'my_project' package
pytest --cov=my_project
```

## Coverage Reports

`pytest-cov` can generate reports in several formats.

- **Terminal Report:** The default report, shown in the terminal after the test run.
- **HTML Report:** A detailed, interactive report that you can open in your browser. This is great for exploring coverage results.
- **XML Report:** Useful for CI/CD integration.

```bash
# Generate an HTML report in the 'htmlcov' directory
pytest --cov=my_project --cov-report=html
```

## `.coveragerc` Configuration

You can configure `pytest-cov` using a `.coveragerc` file. This allows you to set default options and exclude files or lines from the coverage report.

```ini
# .coveragerc
[run]
source = my_project
omit =
    # Exclude auto-generated files
    my_project/version.py
    # Exclude experimental features
    my_project/experimental/*

[report]
# Fail if the total coverage is below 90%
fail_under = 90
```
