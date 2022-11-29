#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import requests
import random

app = Flask(__name__)

info = {
        'Hall' : {
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
                'north': 'Bathroom',
                'item'  : 'key'
            },

        'Kitchen' : {
                'north' : 'Hall',
                'east'  : 'Garden',
                'item'  : 'monster',
            },
        'Dining Room' : {
                'west' : 'Hall',
                'south': 'Garden',
                'item' : 'potion'
            },
        'Garden' : {
                'north' : 'Dining Room',
                'west'  : 'Kitchen',
                'item'  : 'map'
            },
        'Bathroom' : {
                'south' : 'Hall',
                'item'  : 'saw'
        }
}
#landing page 
@app.route("/")
@app.route("/home")
@app.route("/home.html")
def home():
    return render_template("home.html")

# game info
@app.route("/aboutthegame")
@app.route("/aboutthegame.html")
def gameinfo():
    return render_template("aboutthegame.html")

@app.route("/data")
def data():
    return info

@app.route("/room")
def room():
    currentRoom = random.choice(list(info.keys()))
    return currentRoom

@app.route("/status/<room>")
def status(room):
    return render_template("index.html", name = room, data = info)

@app.route("/map.html")
@app.route("/map")
def map():
    return render_template('map.html')
#if __name__ == "__main__":
app.run(host="0.0.0.0", port=2224)
