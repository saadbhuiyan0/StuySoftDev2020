#Saad Bhuiyan
#SoftDev1 pd2
#K<n> -- <Title/Topic/Summary>
#<yyyy>-<mm>-<dd>  

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/form")
def form():
    print(app)
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "form submitted"

if __name__ == "__main__":
    app.debug = True
    app.run()