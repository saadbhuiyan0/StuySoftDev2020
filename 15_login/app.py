#Saad Bhuiyan and Benjamin Avrahami
#SoftDev1 pd2
#K12 -- Using Python, Flask, Jinja2, and HTML to create a form and custom response.
#2019-09-26 

from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

teamName = "Team Cod"
teamMembers = "Saad Bhuiyan and Coby Sontag"

@app.route("/")
def root():
    print(app)
    return render_template("login.html", 
                            teamName = teamName,
                            teamMembers = teamMembers
    )

myUsername = "teamCod"
myPassword = "fishy"

@app.route("/login")
def authenticate():
    if request.form["username"] == myUsername and request.form["password"] == myPassword
        render_template("welcome.html",
                        username = myUsername)
    else
        return render_template("response.html", 
                            teamName = teamName,
                            teamMembers = teamMembers,
                            name = request.args['name'],
                            donation = request.args['donation'],
                            method = request.method
    )

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.debug = True
    app.run()