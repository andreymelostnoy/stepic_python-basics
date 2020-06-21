import requests
import json

api_url = "https://api.artsy.net/api/artists/{artist}"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3Rf" \
        "YXBwbGljYXRpb24iOiI1ZWVmMWIyNDZmOWQxMDAwMGRkNjdhZjEiLCJleHAiOjE1O" \
        "TMzMzMxNTcsImlhdCI6MTU5MjcyODM1NywiYXVkIjoiNWVlZjFiMjQ2ZjlkMTAwMD" \
        "BkZDY3YWYxIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjVlZWYxYjI1OTIxMWNhMDA" \
        "wZWY3MTlkMyJ9.m4Wx-yqnTfQiqqoCPQfdSBDUxLeBfXxrG2CC6jS8dPw"
headers = {"X-Xapp-Token": token}
artists = {}

with open("dataset_24476_4.txt", "r", encoding="utf-8") as file:
    for artist in file:
        r = requests.get(api_url.format(artist=artist.strip()), headers=headers)
        j = json.loads(r.text)
        if r.status_code == 404:
            pass
        else:
            artists[j["sortable_name"]] = j["birthday"]

for artist in sorted(artists.items(), key=lambda para: para[1]):
    print(artist[0])
