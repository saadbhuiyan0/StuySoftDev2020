# Team Blue Jays - Saad Bhuiyan and Biraj Chowdhury
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-07


from pymongo import MongoClient
from bson.json_util import loads


def data_to_db(col, file):
	f = open(file, "r")
	item = ""
	for line in f:
		item += line
	item = loads(item)
	col.insert(item)
	print("added data to MongoDB")


def get_players_by_first_name(name, col):
	results = col.find({"first_name": name})
	json = {}
	for item in results:
		json.append(item)


def get_players_by_last_name(name, col):
	results = col.find({"last_name": name})
	json = {}
	for item in results:
		json.append(item)


def get_players_by_position(position, col):
	results = col.find({"position": position})
	json = {}
	for item in results:
		json.append(item)


def get_players_by_team_name(name, col):
	results = col.find({"team.full_name": name})
	json = {}
	for item in results:
		json.append(item)


def get_players_by_division(division, col):
	results = col.find({"team.division": division})
	json = {}
	for item in results:
		json.append(item)


def get_players_by_conference(conference, col):
	results = col.find({"team.conference": conference})
	json = {}
	for item in results:
		json.append(item)
