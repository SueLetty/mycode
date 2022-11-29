#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
@app.route("/data")
def data():
    ## A dictionary linking a room to other rooms
    data = {

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
    return data

rooms = ["Hall", "Kitchen", "Dining Room", "Garden"]
@app.route("/room")
def room():
    curroom = random.choice(rooms)
    return curroom

@app.route("/status/<room>")
def status(room):
    dataurl = "https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/data"
    data = requests.get(dataurl).json() 
    print(data)
    return render_template("index.html", name = room, data = data)

@app.route("/map")
def map():
    return render_template('map.html')
#if __name__ == "__main__":
app.run(host="0.0.0.0", port=2224)
