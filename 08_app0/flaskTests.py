from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    #print(__name__)
    print("Home")
    return "Hello World!"
    #return "Changing stuff test."

@app.route("/test")
#the route is an extension of the main page (proper term?)
def test_route():
    print("What does print do?")
    return "What does return do?"
    #returns what shows up on the page

@app.route("/second")
def second():
    print("Still unsure what print does.")
    return "Second is the best."

@app.route("/final")
def finalFunctionName():
    print("I figured out what print does!")
    #prints the text in the command prompt showing where the user is
    #or route being interacted with (?) not sure how to word
    return "I got the hang of this!"

if __name__ == "__main__":
    app.debug = True
    #app.debug = False
    app.run()
