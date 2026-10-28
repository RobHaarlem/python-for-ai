from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()


# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")
password = os.environ.get("PASSWORD_ROB")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
print(f"Password Rob: {password}")


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))
