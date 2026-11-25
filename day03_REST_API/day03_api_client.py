import requests

def get_api_data(url):
    try:
        response = requests.get(url, timeout=10)

        print("Status Code:", response.status_code)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Convert JSON to Python object
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: API request timed out")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.RequestException as e:
        print("API Communication Error:", e)

    return None


url = "https://jsonplaceholder.typicode.com/posts/1"

result = get_api_data(url)

if result:
    print("\nAPI Data Retrieved Successfully")
    print("Post ID:", result["id"])
    print("Title:", result["title"])
    print("User ID:", result["userId"])
else:
    print("No data available")