#Saad Bhuiyan and Coby Sontag
#SoftDev1 pd2
#K15 -- Create a user log in experience
#2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

correctUsername = "teamCod"
correctPassword = "fishAndChips"
loggedIn = False

@app.route("/")
def root():
    if loggedIn:
        print("redirect to /welcome from /")
        return redirect(url_for("welcome"))
    else:
        print("redirect to /login from /")
        return redirect(url_for("login"))

@app.route("/welcome")
def welcome():
    print("welcome page")
    return render_template("welcome.html",
                            username = correctUsername
    )

@app.route("/login")
def login():
    print("log in page")
    return render_template("login.html")

@app.route("/auth")
def auth():
    print("authentication")
    if request.form["username"] == correctUsername:
        if request.form["password"] == correctPassword:
            loggedIn = True
            return redirect(url_for("welcome"))
        else:
            return "wrong password"
    else: 
        return "wrong username"

@app.route("/logout")
def logout():
    print("log out page")
    loggedIn = False
    return "Thanks for visiting!"

if __name__ == "__main__":
    app.debug = True
    app.run()