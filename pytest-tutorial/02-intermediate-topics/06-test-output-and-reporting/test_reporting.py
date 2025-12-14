# test_reporting.py

def test_print_output(capsys):
    """
    This test demonstrates how to use the 'capsys' fixture to capture
    output sent to stdout and stderr.
    """
    # Print some text to stdout
    print("hello world")

    # The capsys.readouterr() method returns a tuple with the captured
    # stdout and stderr as strings.
    captured = capsys.readouterr()

    # Assert that the captured output is correct
    assert captured.out == "hello world\\n"
    assert captured.err == ""

def test_error_output(capsys):
    """
    This test demonstrates capturing output to stderr.
    """
    import sys

    # Write some text to stderr
    sys.stderr.write("error message")

    # Read the captured output
    captured = capsys.readouterr()

    # Assert that the stderr output is correct
    assert captured.err == "error message"
