import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
print("Headers:", response.headers)

data = response.json()

print("\nJSON response:")
print(data)

print("\nPost Title:", data["title"])
print("Post ID:", data["id"])
print("User ID:", data["userId"])
