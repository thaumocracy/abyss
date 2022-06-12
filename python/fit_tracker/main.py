import requests
import datetime as dt

API_ID = ''
API_KEY = ''

sheets_url = 'https://api.sheety.co/'
sheets_headers = {
    "Authorization": 'Bearer'
}

next_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
next_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

activity = input('Whadda ya do today?')
if activity:
    next_config = {
        "query": activity,
        "gender": "male",
        "weight_kg": 130,
        "height_cm": 172,
        "age": 30
    }

    resp = requests.post(url=next_url, headers=next_headers,
                         json=next_config).json()

    x = dt.datetime.now()
    data = resp['exercises'][0]
    print(data)
    sheets_config = {
        "workout": {
            "date": x.strftime("%x"),
            "time": x.strftime("%X"),
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }
    sheets_resp = requests.post(
        url=sheets_url, headers=sheets_headers, json=sheets_config).json()
