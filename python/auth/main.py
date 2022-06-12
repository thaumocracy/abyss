import requests
print(requests.get('https://api.github.com/user', auth=('', '')))