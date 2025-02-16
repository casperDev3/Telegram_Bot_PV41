import requests
from constants.main import BASE_URL

def get_all_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    return response.json()

def get_all_categories():
    url = f"{BASE_URL}/products/categories"
    response = requests.get(url)
    return response.json()