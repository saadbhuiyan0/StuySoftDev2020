#Jionghao Wu and Saad Bhuiyan
#SoftDev
#K17 :: No Trouble
#Oct 9 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================



command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"    #creates the table students with rows name, age and id
c.execute(command)    # run SQL statement

with open('students.csv') as file: #open csvfile
    file = csv.DictReader(file) #read through file using DictReader
    for row in file: # goes through each row of the file
        command = "INSERT INTO students VALUES(" + "\"" + row["name"] + "\"" +", " + row["age"] + ", " + row["id"] + ");" # we can loop like this because the first row become fieldnames
        c.execute(command) #run command

# to test it in the terminal (thanks to Coyote's team)
# command = "SELECT * FROM students;"
# c.execute(command)
# print(c.fetchall())


command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"    #creates the table courses with rows code, mark and id
c.execute(command)    # run SQL statement

with open('courses.csv') as file: #open csvfile
    file = csv.DictReader(file) #read through file using DictReader
    for row in file: # goes through each row of the file
        command = "INSERT INTO courses VALUES(" + "\"" + row["code"] + "\"" +", " + row["mark"] + ", " + row["id"] + ");" # we can loop like this because the first row become fieldnames
        c.execute(command) #run command

#==========================================================

db.commit() #save changes
db.close()  #close database
