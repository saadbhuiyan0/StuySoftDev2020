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
    # print("\n\n\n")
    # print("*** DIAG: this Flask obj***")
    # print(app)
    # print("*** DIAG: request obj ****")
    # print(request)
    # print("*** DIAG: request.args ****")
    # print(request.args)
    print("*** DIAG: request.args['username'] ****")
    print(request.args['username'])
    # print("*** DIAG: request.headers ****")
    # print(request.headers)
    return render_template("response.html")

if __name__ == "__main__":
    app.debug = True
    app.run()