print(f"API Key: {API_KEY}")
print(f"Request URL: https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}")

# Then proceed with the request
response = requests.post(url, json=data, headers=headers)