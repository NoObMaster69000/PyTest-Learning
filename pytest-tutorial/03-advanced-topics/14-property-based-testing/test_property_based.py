# test_property_based.py
from hypothesis import given, strategies as st
from my_library import encode, decode

# Hypothesis will run this test many times with different inputs,
# trying to find a case where the property fails.

# The property we are testing is that for any string `s`,
# `decode(encode(s)) == s`.
@given(st.text())
def test_decode_inverts_encode(s):
    """
    This is a property-based test. It checks that the `decode` function
    is the inverse of the `encode` function for any string.

    Hypothesis will discover a bug in the `encode` function. The current
    implementation does not handle runs of more than 9 characters correctly.
    Hypothesis will find a simple failing example, like "aaaaaaaaaa",
    and report it.
    """
    assert decode(encode(s)) == s

# A more targeted test to demonstrate a more complex strategy.
# This strategy generates strings containing only lowercase letters,
# and with a minimum size of 1.
@given(st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=1))
def test_encode_decode_with_specific_alphabet(s):
    """
    A property-based test with a more specific strategy.
    """
    assert decode(encode(s)) == s
