# Team "bar"
# Saad Bhuiyan & Ethan Chen
# SoftDev1 pd2
# K#17: No Trouble
# 2019-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE= "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"

#foo = c.execute(q)

#for bar in foo:
   # print(bar)

getGrades = "SELECT students.id, mark FROM students, courses WHERE students.id = courses.id;"
grades = c.execute(getGrades)

for grade in grades:
    print(grade[0])

dict
if (grade
#==========================================================

db.commit() #save changes
db.close()  #close database


