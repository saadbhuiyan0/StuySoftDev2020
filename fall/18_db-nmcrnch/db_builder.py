# Team "bar"
# Saad Bhuiyan & Ethan Chen
# SoftDev1 pd2
# K#18: Average
# 2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE= "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);")

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES('%s', %d, %d);" % (row['code'], int(row['mark']), int(row['id'])))

c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);")

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students VALUES('%s', %d, %d);" % (row['name'], int(row['age']), int(row['id'])))

#==========================================================

db.commit() #save changes
db.close()  #close database


