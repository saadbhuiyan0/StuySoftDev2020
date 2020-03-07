# Saad Bhuiyan, Biraj Chowdhury
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-07


# We compiled our own dataset by using data available from the Balldontlie API
# We made API calls to collect all the JSON data for each player they had.
# This includes data such as name, position, team, other team information, etc. 
# We stored all that data in our own JSON file with all 3000+ players.
# Balldontlie API: https://www.balldontlie.io/api/v1/players


import pymongo, json, pprint
from bson.json_util import loads
from api import api_data_json
from parse import add_to_db, getPlayerName, getTeamName, getConference, getDivision, getPosition


client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['teamname'] # does not have to exist
col = db['nba']


if col.count() == 0:
	print('hello dere')
	api_data_json()
	add_to_db(col, "balldontlie.json")


#answers = col.find({})
#for line in answers:
#	print(line)


#getPlayerName("James",col)
#getTeamName("Pacers", col)
#getConference("East", col)
#getDivision("Central", col)
getPosition("C", col)