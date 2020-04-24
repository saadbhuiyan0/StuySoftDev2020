# Justin Chen and Saad Bhuiyan
# SoftDev2 pd02 and pd09
# K18 -- Come Up For Air
# 2020-04-21

from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

# Route used to store json
@app.route("/data")
def data():
    # Load in JSON file
    with open("data.json") as myFile:
        myData = json.load(myFile)
    myJSON = jsonify(myData)

    return myJSON

if __name__ == "__main__":
    app.debug = True
    app.run()