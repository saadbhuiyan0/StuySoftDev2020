# Saad Bhuiyan, Biraj Chowdhury
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-07


from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint


def data_to_db(col, file):
	f = open(file, "r")
	item = ""
	for line in f:
		item += line
	item = loads(item)
	col.insert(item)
	print("added data to MongoDB")


def print_player_info(item):
	pprint(item)


def get_players_by_first_name(name, col):
	results = col.find({"first_name": name})
	for item in results:
		print_player_info(item)


def get_players_by_last_name(name, col):
    results = col.find({"last_name": name})
	for item in results:
		print_player_info(item)


def get_players_by_position(position, col):
    results = col.find({"position": position})
	for item in results:
		print_player_info(item)


def get_players_by_team_name(name, col):
	results = col.find({"team.full_name": name})
	for item in results:
		print_player_info(item)


def get_players_by_division(division, col):
	results = col.find({"team.division": division})
	for item in results:
		print_player_info(item)


def get_players_by_conference(conference, col):
	results = col.find({"team.conference": conference})
	for item in results:
		print_player_info(item)
