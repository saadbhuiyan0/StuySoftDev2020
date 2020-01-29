#Saad Bhuiyan
#SoftDev1 pd2
#K6 -- Build a dictionary from a csv file and get a random (weighted) occupation
#2019-09-16

import csv
import random


occupations = {}

with open( "occupations.csv") as csv_file: #csv to dictionary
    csv_reader = csv.reader( csv_file, delimiter = ",") 
    for row in csv_reader:
        occupations[ row[0]] = row[1] 
    del occupations[ "Job Class"] #delete header
    del occupations[ "Total"] #delete footer

#for occupation, percentage in occupations.items():
    #print( occupation, " - ", percentage)


def randomOccupation():
    jobClass = []
    percentage = []
    for occupation in occupations:
        jobClass.append( occupation)
        percentage.append( float( occupations[ occupation])) #percentage should be float
    return random.choices( jobClass, weights = percentage, k = 1)

print( randomOccupation())
