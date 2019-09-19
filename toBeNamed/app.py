#Saad Bhuiyan
#SoftDev1 pd2
#classwork working with static folder and html
#2019-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def route1():
    print(__name__)
    return "first route"

@app.route("/1")
def route2():
    print(__name__)
    print(__name__)
    return "second route"

@app.route("/2")
def route3():
    print(__name__)
    print(__name__)
    print(__name__)
    return "third route"

@app.route("/static")
def helloWorld():
    print(__name__)
    coll = {0, 1, 2, 3, 4, 5}
    return "hello world"

if __name__ == "__main__":
    app.debug = True
    app.run()
