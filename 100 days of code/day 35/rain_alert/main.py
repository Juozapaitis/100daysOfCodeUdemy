import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

load_dotenv('100 days of code//.gitignore')

ACCOUNT_SID = os.getenv('account_sid')
AUTH_TOKEN = os.getenv('auth_token')
APPID = os.getenv('appid')
FROM_NUMBER = os.getenv('from_number')
TO_NUMBER = os.getenv('to_number')

parameters = {
    'lat': 51.509865,
    'lon': -0.118092,
    'exclude': 'current,minutely,alerts,daily',
    'appid': APPID,
}


# < 700 take an umbrella
response = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False

for data in weather_slice:
    condition_code = (data['weather'][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages .create(
                     body="It's going to rain today. Remember to bring an umbrella ☔",
                     from_=FROM_NUMBER,
                     to=TO_NUMBER
                 )

print(message.status)

# print(data['hourly'][0]['weather'][0]['id'])