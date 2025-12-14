# app.py
import os
import requests

def get_user_name(user_id):
    """
    Fetches a user's name from an external API.
    """
    api_url = f"https://api.example.com/users/{user_id}"
    response = requests.get(api_url)
    return response.json()["name"]

def get_api_key():
    """
    Retrieves the API key from an environment variable.
    """
    return os.environ.get("API_KEY")
