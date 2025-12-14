# test_integration.py
import pytest
import json

# This module simulates a simple data processing application that
# reads from and writes to the file system.

class DataProcessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def process_file(self, input_filename, output_filename):
        """
        Reads a JSON file, extracts the "name" field, and writes a
        greeting to an output file.
        """
        input_path = self.data_dir / input_filename
        output_path = self.data_dir / output_filename

        try:
            with open(input_path, 'r') as f:
                data = json.load(f)

            name = data["name"]
            greeting = f"Hello, {name}!"

            with open(output_path, 'w') as f:
                f.write(greeting)

            return True
        except (IOError, KeyError):
            return False

# The `tmp_path` fixture provides a temporary directory unique to the test function.
# It's a `pathlib.Path` object, which makes file system operations easy.
def test_data_processor(tmp_path):
    """
    This is an integration test for the DataProcessor class.
    It uses the `tmp_path` fixture to create a temporary directory for
    the test, ensuring that the test does not depend on or affect the
    real file system.
    """
    # `tmp_path` is the path to the temporary directory.
    # We can create subdirectories and files within it.
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Create the input file.
    input_file = data_dir / "input.json"
    input_file.write_text('{"name": "Jules"}')

    # Create an instance of the class we're testing.
    processor = DataProcessor(data_dir)

    # Call the method we want to test.
    output_file = "output.txt"
    result = processor.process_file("input.json", output_file)

    # Assert that the method behaved as expected.
    assert result is True

    # Assert that the output file was created with the correct content.
    output_path = data_dir / output_file
    assert output_path.read_text() == "Hello, Jules!"
