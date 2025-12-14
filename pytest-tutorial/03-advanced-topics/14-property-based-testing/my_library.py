# my_library.py

def encode(input_string):
    """
    A simple encoding function.
    There is a bug in this function that Hypothesis will help us find.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # A simple run-length encoding implementation.
    if not input_string:
        return ""

    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            result.append(str(count) + input_string[i-1])
            count = 1
    result.append(str(count) + input_string[-1])
    return "".join(result)

import re

def decode(encoded_string):
    """Decodes a string encoded by the `encode` function."""
    if not encoded_string:
        return ""

    # Use a regular expression to find all occurrences of a number followed by a character.
    # This correctly handles multi-digit numbers.
    parts = re.findall(r'(\d+)(.)', encoded_string)

    # Reconstruct the original string.
    result = [char * int(count) for count, char in parts]

    return "".join(result)
