import requests
from datetime import datetime as dt

USERNAME = ''
TOKEN = ''
pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_config = {
    "id": "graph1",
    "name": "test_graph",
    "unit": 'Km',
    "type": 'float',
    "color": 'ajisai'
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
graph1_endpoint = f"{graph_endpoint}/graph1"
current_date = dt.now()
current_month = f'{current_date.month}'
DATE = f"{current_date.year}{current_month.zfill(2)}{current_date.day}"

graph1_config = {
    "date": DATE,
    "quantity": '3'
}
print(DATE)

# resp = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)
# print(resp)

update_config = {
    "quantity": '10'
}
resp = requests.put(url=f"{graph1_endpoint}/20210302",
                    json=update_config, headers=headers)
print(resp)
