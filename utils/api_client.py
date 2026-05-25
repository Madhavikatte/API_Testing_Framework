import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
API_KEY = os.getenv("REQRES_API_KEY")

def get_headers():
    """Returns headers required for every request"""
    return {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

BASE_URL = "https://reqres.in/api"


def get(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}", headers=get_headers())

def post(endpoint, payload):
    return requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=get_headers())

def put(endpoint, payload):
    return requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=get_headers())

def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}", headers=get_headers())

