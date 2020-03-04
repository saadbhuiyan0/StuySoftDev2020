# Jackson Zou, Saad Islam Bhuiyan
# SoftDev pd9
# K10 -- Import/Export Bank
# 2020-03-02


from pymongo import MongoClient
from bson.json_util import loads

def add_to_db( col , file ):
	f = open(file, "r")
	final = ""
	for line in f:
		final += line
	#print(final)
	final = loads(final)
	#print(final)
	col.insert(final)
	print("info gotten")

def printPlayer( item ):
	final = ""
	final += "Name: " + item['first_name'] + " " + item['last_name'] + " Team: " + item["team"]["full_name"]
	print(final)

def getPlayerName( name, col ):
	final = col.find({"first_name": name})
	for item in final:
		printPlayer( item )

def getTeamName( name, col ):
	final = col.find({"team.name": name})
	for item in final:
		printPlayer( item )

def getConference( conference, col ):
	final = col.find({"team.conference": conference})
	for item in final:
		printPlayer( item )

def getDivision( division, col ):
	final = col.find({"team.division": division})
	for item in final:
		printPlayer( item )

def getPosition( position, col ):
	final = col.find({"position": position})
	for item in final:
		printPlayer ( item )
