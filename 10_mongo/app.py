# Saad Bhuiyan and Jackson Zou
# SoftDev2 pd9
# K10 -- Mongo
# 2020-03-01


from pymongo import MongoClient
from bson.json_util import loads
import json
import urllib.request


def api_data_for_page(page):
    api_call = urllib.request.urlopen("https://www.balldontlie.io/api/v1/players?per_page=100&page=" + str(page))
    response = api_call.read()
    response_data = json.loads(response)
    players = response_data["data"]
    return players

def api_data_json():
    with open("balldontlie.json", "w") as f:
        data = {"players":[]}
        players = data["players"]
        for page in range(1,33):
            api_data = api_data_for_page(page)
            for player in range(100):
                players.append(api_data[player])
        api_data = api_data_for_page(33)
        for player in range(66):
            players.append(api_data[player])
        json.dump(data, f)

try:
    f = open("data.json")
except FileNotFoundError:
    api_data_json()


