# Debugging and Troubleshooting

Pytest provides several features to help you debug failing tests.

## PDB Integration (`--pdb`)

The `--pdb` flag will automatically start the Python debugger (PDB) at the point of failure. This allows you to inspect the state of your program and understand why the test is failing.

```bash
pytest --pdb
```

## Rerunning Failed Tests (`--lf`, `--ff`)

- `--lf` (`--last-failed`): Run only the tests that failed on the last run. This is useful when you're fixing a bug and want to quickly rerun the relevant tests.
- `--ff` (`--failed-first`): Run all tests, but run the ones that failed last time first.

## Verbose Tracebacks

By default, pytest truncates tracebacks to be more readable. If you need more detail, you can use the `--tb` option.

- `--tb=long`: Show the full traceback.
- `--tb=short`: Show a shorter, more concise traceback (the default).
- `--tb=no`: Don't show any traceback.

## Print Debugging (`-s`)

If you're using `print()` statements for debugging, you'll need to use the `-s` flag to see the output. By default, pytest captures all output.

```bash
pytest -s
```

## Logging Configuration

Pytest can also capture and display log messages from the standard `logging` module.

- `--log-cli-level`: Set the minimum log level to be displayed.
- `--log-file`: Redirect log messages to a file.

```bash
pytest --log-cli-level=INFO
```
