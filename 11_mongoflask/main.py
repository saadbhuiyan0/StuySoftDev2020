# Saad Bhuiyan, Biraj Chowdhury
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-07


# We compiled our own dataset by using data available from the Balldontlie API
# We made API calls to collect all the JSON data for each player they had.
# This includes data such as name, position, team, other team information, etc. 
# We stored all that data in our own JSON file with all 3000+ players.
# Balldontlie API: https://www.balldontlie.io/api/v1/players


from pymongo import MongoClient
from bson.json_util import loads
from api import api_data_to_json
from parse import data_to_db, get_players_by_first_name, get_players_by_last_name, get_players_by_position, get_players_by_team_name, get_players_by_division, get_players_by_conference


client = MongoClient('localhost', 27017) # port 27017
db = client['nba'] # does not have to exist
col = db['balldontlie']


if col.count() == 0:
	print("building database")
	api_data_to_json()
	data_to_db(col, "balldontlie.json")


get_players_by_first_name("Mitchell", col)
# get_players_by_last_name("Robinson", col)
# get_players_by_position("C", col)
# get_players_by_team_name("New York Knicks", col)
# get_players_by_division("Atlantic", col)
# get_players_by_conference("East", col)
