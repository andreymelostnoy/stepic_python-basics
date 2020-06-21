import requests


api_url = "http://numbersapi.com/{number}/math"
params = {
    "json": "true"
}

with open("dataset_24476_3.txt", "r") as file:
    for number in file:
        r = requests.get(api_url.format(number=number.strip()), params=params)
        if r.status_code == 404:
            print("Boring")
        elif r.json()["found"]:
            print("Interesting")
        else:
            print("Boring")
