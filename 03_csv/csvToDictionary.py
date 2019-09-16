import csv
import random

occupations = {}

with open( "occupations.csv") as csv_file: #csv to dictionary
    csv_reader = csv.reader( csv_file, delimiter = ",") 
    for row in csv_reader:
        occupations[ row[0]] = float(row[1]) #input should be float
    del occupations[ "Job Class"] #delete header
    del occupations[ "Total"] #delete footer

#for occupation, percentage in occupations.items():
    #print( occupation, " - ", percentage)

def randomOccupation():
    
