# Test Output and Reporting

Pytest provides several ways to control the output and reporting of your test runs.

## Verbose Output

You can get more detailed output by using the `-v` and `-vv` flags.

```bash
# Verbose output
pytest -v

# Even more verbose output
pytest -vv
```

## Capturing Output

By default, pytest captures all output to `stdout` and `stderr`. You can access this captured output using the `capsys` fixture.

```python
def test_print_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\\n"
```

## JUnit XML Reports

For integration with continuous integration (CI) systems, you can generate a JUnit XML report.

```bash
pytest --junitxml=report.xml
```

## HTML Reports

The `pytest-html` plugin can be used to generate a self-contained HTML report.

**Installation:**
```bash
pip install pytest-html
```

**Usage:**
```bash
pytest --html=report.html
```
