import os
import requests
from dotenv import load_dotenv

load_dotenv()

# USING THE WEATHER API
WEATHER_URL = " http://api.weatherapi.com/v1/current.json"
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]
city_weather = "Zagora"

parameters = {
    "key": WEATHER_API_KEY,
    "q": city_weather,
}

response = requests.get(url=WEATHER_URL, params=parameters)
response.raise_for_status()
data = response.json()
city = data["location"]["name"]
temperature = data["current"]["temp_c"]
print(f"Current temperature for {city}:\n{temperature} Celsius")

# TODO: BUILD THE WEBHOOK USING: discordwebhook.py






