# test_parametrization.py
import pytest

# The @pytest.mark.parametrize decorator allows you to run a test with multiple sets of inputs.
# The first argument is a string of comma-separated parameter names.
# The second argument is a list of tuples, where each tuple contains the values for the parameters.
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 10, 20),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(x, y, expected):
    """
    This test will be run five times with different values for x, y, and expected.
    """
    assert x + y == expected

# You can provide custom test case identifiers (IDs) to make the test output more readable.
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3+5", 8),
        ("2*4", 8),
        ("6-2", 4),
    ],
    ids=["addition", "multiplication", "subtraction"]
)
def test_eval_with_ids(test_input, expected):
    """
    The test IDs will be shown in the test report, making it easier to identify
    which test case failed.
    """
    assert eval(test_input) == expected

# Indirect parametrization allows you to apply fixtures to your parametrized values.
# The `indirect=True` argument tells pytest to treat the parametrized value as a
# request for a fixture with the same name.
@pytest.fixture
def double_value(request):
    """
    A fixture that takes a parametrized value and doubles it.
    The `request.param` attribute holds the value from the parametrize decorator.
    """
    return request.param * 2

@pytest.mark.parametrize("double_value", [1, 2, 3], indirect=True)
def test_indirect_parametrization(double_value):
    """
    This test uses indirect parametrization. For each run, the `double_value` fixture
    will be called with the corresponding value from the parametrize decorator (1, 2, or 3).
    The test function will then receive the return value of the fixture.
    """
    assert double_value in [2, 4, 6]
