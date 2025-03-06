import requests

API_KEY = "your_api_key_here"  # Replace with your API key
BASE_URL = "https://v6.exchangerate-api.com/v6"

def get_exchange_rate(base, target):
    url = f"{BASE_URL}/{API_KEY}/latest/{base}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rate = data["conversion_rates"].get(target)
        if rate:
            print(f"Exchange Rate ({base} → {target}): {rate}")
        else:
            print("Invalid target currency.")
    else:
        print("Error:", data["error-type"])

if __name__ == "__main__":
    base = input("Enter base currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()
    get_exchange_rate(base, target)
