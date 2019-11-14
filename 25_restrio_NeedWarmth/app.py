#Need Warmth -- Saad Bhuiyan and Justin Chen
#SoftDev1 pd2
#K25 -- Many APIs in One Flask App
#2019-11-13  

from flask import Flask, render_template
import urllib3
import json
from random import randint

app = Flask(__name__)

#render template for Balldontlie API specifically querying kyrie (to find Kyrie Irving)
@app.route("/balldontlie")
def balldontlie():
    player = "kyrie"
    print(__name__)
    print("Balldontlie " + player)
    api_call = "https://www.balldontlie.io/api/v1/players?search=" + player
    http = urllib3.PoolManager()
    response = http.urlopen("GET", api_call)
    data = json.loads(response.data)
    # return data
    player = data["data"][0]
    return render_template("balldontlie.html",
                            first_name=player["first_name"],
                            last_name=player["last_name"],
                            team=player["team"]["full_name"],
                            position=player["position"],
                            height_feet=player["height_feet"],
                            height_inches=player["height_inches"],
                            weight=player["weight_pounds"])

#render template for MetaWeather API displaying weather in woeid 2459115 (New York) for today and the next 5 days
@app.route("/metaweather")
def city_bike():
    location_id = str(2459115)
    print(__name__)
    print("MetaWeather for " + location_id)
    api_call = "https://www.metaweather.com/api/location/" + location_id
    http = urllib3.PoolManager()
    response = http.urlopen("GET", api_call)
    data = json.loads(response.data)
    weather = data["consolidated_weather"]
    # return data
    return render_template("metaweather.html",
                            location=data["title"],
                            date_0=weather[0]["applicable_date"],
                            weather_type_0=weather[0]["weather_state_name"],
                            max_temp_0=weather[0]["max_temp"],
                            min_temp_0=weather[0]["min_temp"],
                            date_1=weather[1]["applicable_date"],
                            weather_type_1=weather[1]["weather_state_name"],
                            max_temp_1=weather[1]["max_temp"],
                            min_temp_1=weather[1]["min_temp"],
                            date_2=weather[2]["applicable_date"],
                            weather_type_2=weather[2]["weather_state_name"],
                            max_temp_2=weather[2]["max_temp"],
                            min_temp_2=weather[2]["min_temp"],
                            date_3=weather[3]["applicable_date"],
                            weather_type_3=weather[3]["weather_state_name"],
                            max_temp_3=weather[3]["max_temp"],
                            min_temp_3=weather[3]["min_temp"],
                            date_4=weather[4]["applicable_date"],
                            weather_type_4=weather[4]["weather_state_name"],
                            max_temp_4=weather[4]["max_temp"],
                            min_temp_4=weather[4]["min_temp"],
                            date_5=weather[5]["applicable_date"],
                            weather_type_5=weather[5]["weather_state_name"],
                            max_temp_5=weather[5]["max_temp"],
                            min_temp_5=weather[5]["min_temp"])

#render template for XKCD API and displaying a random comic
@app.route("/xkcd")
def xkcd():
    random_number = str(randint(1,2227)) # max number should be the most recent comic
    print(__name__)
    print("xkcd")
    api_call = "http://xkcd.com/" + random_number +"/info.0.json"
    http = urllib3.PoolManager()
    response = http.urlopen("GET", api_call)
    data = json.loads(response.data)
    return render_template("xkcd.html",
                            number=random_number,
                            title=data["title"],
                            image_src=data["img"],
                            image_alt=data["alt"])

if __name__ == "__main__":
    app.debug = True
    app.run()
