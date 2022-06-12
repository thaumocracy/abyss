# weather api
import requests
from twilio.rest import Client

city = 'Moscow'
# api_call = f'api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
# api.openweathermap.org/data/2.5/weather?q=Moscow&appid=

weather_params = {
    "lat": 55.755825,
    'lon': 37.617298,
    "appid": '',
    "exclude": "current,minutely,daily"
}
api_call_one = f"https://api.openweathermap.org/data/2.5/onecall"
data = requests.get(api_call_one, params=weather_params).json()['hourly'][:12]

going_to_rain = False


def check_hours(data):
    global going_to_rain
    new_data = data[0:12]
    for hour in new_data:
        idx = hour['weather'][0]['id']
        if 200 <= idx <= 531:
            going_to_rain = True


check_hours(data)

if going_to_rain:
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='You might need an umbrella today',
        from_='+1 415 997 3567',
        to='+',
    )
    print(message.status)
