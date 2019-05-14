import googlemaps
import requests
import sys
import datetime
from flask import render_template, Flask

app = Flask(__name__)

#Declarations
token = '' #Enter your Google API Token'
start = '51.966455, 5.995351'
end = '51.948731, 6.064099'
# get Client object
client = googlemaps.Client(key=token)
# Get directions

@app.route("/")
def index():
     now = datetime.datetime.now()
     directions = client.distance_matrix(start,end, departure_time=now)
     distance = directions["rows"][0]["elements"][0]["distance"]["value"]
     return render_template('index.html', distance=distance)

