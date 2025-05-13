import requests

# Make a GET request to the placeholder Api
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if request was successful
if response.status_code == 200:
    data = response.json()          # Parse JSON response
    print(data[:5])          # Print the first five items
else:
    print(f"Error : {response.status_code}") 