#!/usr/bin/python3

import requests
import webbrowser
import os

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
dataurl = "https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/data"
roomurl = "https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/room"
statusurl = "https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/status"
mapurl ="https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/map"
#start at random room
rooms = requests.get(dataurl).json() 
currentRoom = requests.get(roomurl).text

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item 
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')

                ## If a player enters a room with a map
            if 'item' in rooms[currentRoom] and 'map' in rooms[currentRoom]['item']:
                #go to get image from the API
                print("click on the link to get the map")
                print(mapurl)

            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'saw' not in inventory:
        print('A monster has got you... GAME OVER!')
        break

    ## If a player enters a room with a monster and have a saw
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'saw' in inventory:
        print('You defeated the monster! You won!!!')
        break


    ## Define how a player can win
    elif currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

