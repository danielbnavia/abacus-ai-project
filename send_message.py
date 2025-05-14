import requests

# Define the API endpoint and headers
url = "https://api.abacus.ai/chat/send"  # Replace with the actual endpoint
api_key = 's2_00906e19fbd24f6a9fe9c6091c1849a5'  # Replace with your actual API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "appId": "cf92ea59e",  # Replace with your actual app ID
    "message": "Hello, Abacus.AI!"  # Replace with your desired message
}

# Send the request
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
    print("Response from chat app:", response.json())
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)