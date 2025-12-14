# test_coverage.py
from my_module import classify_number

def test_classify_number_positive():
    """Tests the 'positive' branch of the classify_number function."""
    assert classify_number(5) == "positive"

def test_classify_number_zero():
    """Tests the 'zero' branch of the classify_number function."""
    assert classify_number(0) == "zero"

# Note that we are missing a test for the 'negative' branch.
# When you run pytest with the --cov flag, you will see that this
# branch is not covered.
#
# To run coverage analysis on this example, use the following command:
# pytest --cov=my_module
#
# To generate an HTML report, which is great for visualizing coverage:
# pytest --cov=my_module --cov-report=html
#
# After running the command above, open the `htmlcov/index.html` file
# in your browser to see the detailed report.
