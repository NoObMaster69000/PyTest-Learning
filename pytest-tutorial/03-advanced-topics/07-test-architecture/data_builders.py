# data_builders.py

class UserBuilder:
    """
    A Test Data Builder for creating user objects.
    This pattern makes it easy to create test data with different variations.
    """
    def __init__(self):
        self._data = {
            "name": "Default User",
            "email": "default@example.com",
            "is_admin": False,
        }

    def with_name(self, name):
        self._data["name"] = name
        return self

    def with_email(self, email):
        self._data["email"] = email
        return self

    def as_admin(self):
        self._data["is_admin"] = True
        return self

    def build(self):
        return self._data
