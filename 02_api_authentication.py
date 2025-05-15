import requests
import os
from dotenv import load_dotenv

#Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()
# print(data)

for article in data["articles"]:
   print(article["title"])