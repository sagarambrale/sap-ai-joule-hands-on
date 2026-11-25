import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

headers = {
    "Accept": "application/json"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)

print("Final URL:", response.url)
print("Status:", response.status_code)

data = response.json()

print("Records returned:", len(data))
print(data[:1])