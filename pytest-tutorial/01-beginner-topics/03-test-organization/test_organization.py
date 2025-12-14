# test_organization.py

# Standalone test functions are the simplest way to write tests.
def test_standalone_function_one():
    """
    This is a standalone test function.
    """
    assert True

def test_standalone_function_two():
    """
    Another standalone test function.
    """
    x = "hello"
    assert "h" in x

# Test classes can be used to group related tests together.
# The class name should start with "Test".
class TestMyClass:
    """
    This class groups tests related to a specific feature.
    """
    # Test methods are instance methods of the class.
    # The method name should start with "test_".
    def test_method_one(self):
        """
        A test method within a class.
        """
        assert 1 + 1 == 2

    def test_method_two(self):
        """
        Another test method within the same class.
        """
        assert len("pytest") == 6
