# my_module.py

# A simple function that we will mock in our tests.
def get_data_from_api():
    """
    This function would normally make an API call.
    In our test, we'll mock it to avoid making a real network request.
    """
    # In a real application, this might be a slow and expensive operation.
    return "real data"
