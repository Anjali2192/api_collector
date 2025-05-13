import requests

# Your Weatherstack API Key
api_key = "eb3a621ca0e4d3d35eb96aaf920a4597"
city = input("Enter name of the city: ")

# API endpoint with parameters
url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"

# Optional headers (not required by Weatherstack, but useful practice)
headers = {
    "User-Agent": "MyWeatherApp/1.0",  # Identify your app
    "Accept": "application/json"       # Expect JSON response
}

# Make GET request with headers
response = requests.get(url, headers=headers)

# Check response
if response.status_code == 200:
    data = response.json()
    
    if "current" in data:
        temperature = data["current"]["temperature"]
        weather_description = data["current"]["weather_descriptions"]
        humidity = data["current"]["humidity"]
        city_name = data["location"]["name"]
        
        print(f"Weather in {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
    else:
        print("Error in API response:", data)
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")