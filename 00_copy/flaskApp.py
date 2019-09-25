#Saad Bhuiyan
#SoftDev1 pd2
#K<n> -- <Title/Topic/Summary>
#<yyyy>-<mm>-<dd>  

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    #app.debug = False
    app.run()
