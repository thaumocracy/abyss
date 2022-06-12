import requests
from bs4 import BeautifulSoup

USER_ID = ''
CODE = 'K8-NF6Do3vwvugFDfYBYHXh-HmwyvfXePW5bUDJWHP7Vjp_k8zGEU6j_OvciD84K-oOHcDxq7oP4fjmqFl_GTUMLJJVk'
URL = f'https://api.spotify.com/v1/users/{USER_ID}/playlists'

HEADERS = {
    "Authorization": f'Bearer {CODE}',
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def create_playlist(name):
    playlist_config = {
        "name": f"{name}",
        "description": "New playlist description",
        "public": False
    }
    resp = requests.post(URL, json=playlist_config, headers=HEADERS)


def delete_tracks(items):
    data = {
        "tracks": items
    }
    resp = requests.delete('https://api.spotify.com/v1/playlists//tracks', json=data,
                           headers=HEADERS)


def clear_playlist():
    tracks = []
    resp = requests.get(
        "https://api.spotify.com/v1/playlists/", headers=HEADERS)
    for item in resp.json()['tracks']['items']:
        track_config = {"uri": f"spotify:track:{item['track']['id']}"}
        tracks.append(track_config)
    delete_tracks(tracks)


def get_page():
    return requests.get('https://www.billboard.com/charts/hot-100/2000-08-12').text


def compile_tracks():
    tracks = []
    soup = BeautifulSoup(get_page(), 'html.parser')
    track_list = soup.find(name='ol', class_='chart-list__elements')
    track_items = track_list.find_all(
        name='span', class_='chart-element__information')
    for item in track_items:
        artist = item.find(
            name='span', class_='chart-element__information__artist').getText()
        song = item.find(
            name='span', class_='chart-element__information__song').getText()
        tracks.append(f"{artist} {song}")
    return tracks


def get_new_tracks(billboard):
    ids = []
    for item in billboard:
        try:
            resp = requests.get(
                f'https://api.spotify.com/v1/search?q={item}&type=track', headers=HEADERS)
            idx = resp.json()['tracks']['items'][0]['id']
            ids.append(f'spotify:track:{idx}')
        except IndexError:
            print(f'There was an error with: {item}')
    return ids


twozero = compile_tracks()


def push_new_tracks(tracks):
    resp = requests.post(f'https://api.spotify.com/v1/playlists//tracks?uris={",".join(tracks)}',
                         headers=HEADERS)
    print(resp.json())


# push_new_tracks(get_new_tracks(twozero))
