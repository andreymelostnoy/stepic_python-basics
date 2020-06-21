import requests


api_url = "http://numbersapi.com/{number}/math"
params = {
    "json": "json"
}

with open("file.txt", "r") as file:
    for number in file:
        r = requests.get(api_url.format(number=number), params=params)
        if r.json()["found"]:
            print("Interesting")
        else:
            print("Boring")
