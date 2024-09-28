import os
import requests
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook

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
message = f"Current temperature for {city}:\n{temperature} Celsius"

# Creating the Webhook
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1289636312608931953/EmgQd0M2wAABU1nciB1nlXj9_kIzgKVT5Yt9sB1WrTGvJzFoZVkOaVu0bNoPyuL3IfQk",
                         content=message)
response = webhook.execute()







