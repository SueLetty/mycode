#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import random
from pprint import pprint

app = Flask(__name__)

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

rooms = ["Hall", "Kitchen", "Dining Room", "Garden"]
@app.route("/room")
def room():
    curroom = random.choice(rooms)
    return curroom

@app.route("/status/<room>")
def map(room):
    return render_template("index.html", name= room, data= data)

#if __name__ == "__main__":
app.run(host="0.0.0.0", port=2224)
