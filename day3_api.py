import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)

print("Response JSON:")
print(response.json())

if response.status_code == 200:

    data = response.json()

    print("API successful")
    print("Status:", response.status_code)
    print("Customer/User ID:", data["id"])
    print("Name:", data["name"])
    print("Email:", data["email"])

else:
    print("API failed")
    print("Status:", response.status_code)
    print("Response:", response.text)