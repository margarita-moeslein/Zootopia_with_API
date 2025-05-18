import os

import requests
from typing import Any, Dict, List
from dotenv import load_dotenv

API_URL = "https://api.api-ninjas.com/v1/animals?name={}"

# Load variables from .env file into environment
load_dotenv()

def fetch_data(name: str) -> List[Dict[str, Any]]:
    """
    Fetches animals data from the API by the given name.

    Returns:
         A list of animals.
    """
    api_url = API_URL.format(name)
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Please set value for API_KEY in your .env file.")
        return []

    try:
        response = requests.get(api_url, headers={"X-Api-Key": api_key}, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return []




