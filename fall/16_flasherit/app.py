#Saad Bhuiyan and Coby Sontag
#SoftDev1 pd2
#K16 -- Add flashed messages to 15_login and use Jinja inheritance
#2019-10-04

from flask import Flask, render_template, request, session, redirect, url_for, flash
app = Flask(__name__)

app.secret_key = "iDontLikeFish"

teamName ="Team Cod"
teamMembers ="Saad Bhuiyan and Coby Sontag"

correctUsername = "teamCod"
correctPassword = "fishAndChips"

@app.route("/")
def root():
    if not "loginStatus" in session:
        session["loginStatus"] = False
    if (session["loginStatus"]):
        print("redirect to /welcome from /")
        return redirect(url_for("welcome"))
    else:
        print("redirect to /login from /")
        return redirect(url_for("login"))

@app.route("/welcome")
def welcome():
    #flash("You're logged in! Welcome!")
    print("welcome page")
    return render_template("welcome.html",
                            username = session["username"],
                            teamName = teamName,
                            teamMembers = teamMembers
    )

@app.route("/login")
def login():
    #flash("Please fill in your login credentials.")
    print("login page")
    return render_template("login.html",
                            teamName = teamName,
                            teamMembers = teamMembers
    )

@app.route("/auth", methods=["POST"])
def auth():
    print("authentication")
    if request.form["username"] == correctUsername:
        session["username"] = request.form["username"]
        if request.form["password"] == correctPassword:
            session["loginStatus"] = True
            print("valid login redirect to /welcome from /auth")
            return redirect(url_for("welcome"))
        else:
            #flash("Sorry that's the wrong password.")
            session["incorrect"] = "password"
            print("invalid password redirect to /invalidLogin from /auth")
            return redirect(url_for("invalidLogin"))
    else: 
        #flash("Sorry that's the wrong username.")
        session["incorrect"] = "username"
        print("invalid username redirect to /invalidLogin from /auth")
        return redirect(url_for("invalidLogin"))

@app.route("/invalidLogin")
def invalidLogin():
    #flash("Sorry your login information was invalid.")
    print("invalid login")
    return render_template("invalidLogin.html",
                            teamName = teamName,
                            teamMembers = teamMembers,
                            value = session["incorrect"]
    )

@app.route("/logout")
def logout():
    #flash("Good bye! Please come back...")
    print("log out page")
    session["loginStatus"] = False
    return render_template("logout.html",
                            teamName = teamName,
                            teamMembers = teamMembers
    )

if __name__ == "__main__":
    app.debug = True
    app.run()