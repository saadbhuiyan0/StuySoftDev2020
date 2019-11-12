#Saad Bhuiyan
#SoftDev1 pd2
#K24 -- NASA API + Flask Webpage
#2019-11-12  

from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)
api_key="0tIjwlghw1YoRsGOGwHh4PRIUkx5KtvknEbkEelY"

#render template for NASA's Astronomy Picture of the Day from APOD API call
@app.route("/")
def nasa_apod():
    print(__name__)
    print("NASA's Astronomy Picture of the Day")
    api_call = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    http = urllib3.PoolManager()
    response = http.urlopen("GET", api_call)
    data = json.loads(response.data)
    # return data
    return render_template("nasa_apod.html",
                            title=data.get("title"),
                            date=data.get("date"),
                            image=data.get("url"),
                            explanation=data.get("explanation"))

if __name__ == "__main__":
    app.debug = True
    app.run()
