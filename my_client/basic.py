import requests

endpoint = "https://www.github.com"

get_response = requests.get(endpoint)

print(get_response.json())
