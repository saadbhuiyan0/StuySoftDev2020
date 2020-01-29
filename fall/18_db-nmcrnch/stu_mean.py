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

#FACILITATE ADDING ROWS INTO THE COURSES TABLE BY TAKING INPUT FROM THE TERMINAL
print("add rows into the courses table \nend loop by entering nothing")
course = input("Enter course code: ")
mark = input("Enter mark: ")
id = input("Enter id: ")

#until they dont add anything, keep asking for input
while (course != "" and mark != "" and id != ""):
    c.execute("INSERT INTO courses VALUES('{}',{},{})".format(course, int(mark), int(id)))
    course = input("Enter course code: ")
    mark = input("Enter mark: ")
    id = input("Enter id: ")


c.execute("CREATE TABLE stu_avg(id INTEGER, avg INTEGER)")

getGrades = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
grades = c.execute(getGrades) #an array of arrays of name, id, and mark

oldID = amt = total = 0
commands = [] #an array of commands listing what to insert into the table stu_avg

#go through each row to calculate the Average
#CREATES TABLE STU_AVG
#DISPLAYS EACH NAME ID AND AVERAGE
for grade in grades:
    newID = grade[1] #get name of the current row
    if oldID != newID: # if the name doesnt match the one before,
        if oldID != 0: #this is to discard the first occurance of oldID
            commands.append("INSERT INTO stu_avg VALUES({}, {})".format(oldID, total/amt))
            print("Name: {}, ID: {}, Average: {}".format(oldName, oldID, (total/amt)))
        amt = 1 #resets amt
        total = grade[2] #resets total
    if oldID == newID: #if it is the same, the amt increases by 1, and the grade is added to the total
        amt += 1
        total += grade[2]
    oldName = grade[0] #changes the oldname
    oldID = newID #newID becomes the oldID

for command in commands:
    c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
