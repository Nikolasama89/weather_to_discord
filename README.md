# Weather Discord Webhook
This Python project fetches the current weather information for a specific city from the Weather API and sends the data to a Discord channel via a webhook.

## Prerequisites
Make sure you have the following installed:

Python 3.6+
Required Python packages (see below)
An account on Weather API with an API key and
a Discord webhook URL



## Setup Instructions
Clone this repository or copy the script.
Create a .env file in the project directory and add your API key

Replace the placeholder Discord webhook URL in the script with your own webhook URL.
## How to Run
Load your environment variables by running the script.
The script will:
Fetch the current weather data for the specified city.
Send the temperature information to your Discord channel using the webhook.

## Explanation of Key Components
Weather API: The script uses the Weather API to retrieve weather data. The city and API key are passed as parameters to get the temperature in Celsius.
Discord Webhook: A webhook URL is used to send the temperature data to a Discord channel.
.env file: The .env file is used to store the API key securely.


Let me know if you'd like any changes!