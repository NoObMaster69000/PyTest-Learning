# my_module.py

def classify_number(n):
    """
    Classifies a number as positive, negative, or zero.
    This function has multiple branches, making it a good candidate
    for coverage analysis.
    """
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def unused_function():
    """
    This function is intentionally not called by any tests, so it will
    not be covered.
    """
    return "this should not be covered"
