import requests
import datetime as dt

LAT = 55.755825
MIN_LAT = LAT - 5
MAX_LAT = LAT + 5
LNG = 37.617298
MIN_LNG = LNG - 5
MAX_LNG = LNG + 5


def is_iss_above():
    data = requests.get('http://api.open-notify.org/iss-now.json').json()['iss_position']
    if (MIN_LAT < float(data['latitude']) < MAX_LAT) and (MIN_LNG < float(data['longitude']) < MAX_LNG):
        return True
    else:
        return False


def is_dark(lat, lng):
    data = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0').json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    hour = dt.datetime.now().hour
    if hour > sunset or hour < sunrise:
        return True
    else:
        return False

def check_iss():
    if is_iss_above() and is_dark(LAT,LNG):
        print('Reach for the sky!')
    else:
        print('Not above or dark enough')

check_iss()