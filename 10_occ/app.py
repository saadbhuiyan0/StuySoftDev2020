#teamFakeMoonLanding_bhuiyanS_huangT
#SoftDev1 pd2
#K10 -- Using Flask and Jinja2 to present occupations.csv as a table in HTML
#2019-09-20


from flask import Flask, render_template
import csv, random
app = Flask(__name__)

@app.route("/")
def homePage():
    print("moon landing")
    coll = {"the moon landing was fake", "okay maybe it was real", "but birds definitely aren't real"}
    return render_template( 
        'my_foist_template.html',
        foo = "teamFakeMoonLanding", 
        collection = coll)

occupations = {}
jobClass = []
percentage = []

with open( "occupations.csv") as csv_file: #csv to dictionary
    csv_reader = csv.reader( csv_file, delimiter = ",") 
    for row in csv_reader:
        occupations[ row[0]] = row[1] 
    del occupations[ "Job Class"] #delete header
    del occupations[ "Total"] #delete footer

def randomOccupation():
    for occupation in occupations:
        jobClass.append( occupation)
        percentage.append( float( occupations[ occupation])) #percentage should be float
    return random.choices( jobClass, weights = percentage, k = 1)

@app.route("/occupyflaskt")
def occupationscsvToHTML():
    print("occupations csv to html")
    return render_template( 
        'occupations_csv_to_HTML_table.html',
        randomOccupation = randomOccupation(),
        dictionary = zip(jobClass, percentage)
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
