import requests
import os
from twilio.rest import Client
import chardet

api_key = "1d24658b9f114126756515c61bd6dda9"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


parameters = {
    "lat": 50.095051,
    "lon": 14.465340,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False
for hour in range(12):
    weather_code = weather_data["hourly"][hour]["weather"][0]["id"]
    if weather_code < 700:
        # print(f"rain in hour {hour}")
        will_rain = True
    else:
        print(f"no rain in hour {hour}")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_='+17623395958',
        to='+420775653622'
    )
    print(message.status)

