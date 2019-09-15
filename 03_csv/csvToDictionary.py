import csv
import random

occupations = {}

with open( "occupations.csv") as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ",") 
    for row in csv_reader:
        occupations[ row[0]] = row[1]

for occupation, percentage in occupations.items():
    print( occupation, " - ", percentage)
