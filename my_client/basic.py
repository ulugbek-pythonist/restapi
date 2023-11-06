import requests

# endpoint = "https://www.github.com/"
# endpoint = "https://www.httpbin.org/anything/"
# endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint)
print(get_response.status_code)
print(get_response.json())
