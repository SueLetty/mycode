#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    print(pokeapi)

    # part 1 Slicing (No for loop)
    print(pokeapi["sprites"]["front_default"])

    # part 2 Slicing with a for loop
    for x in pokeapi["moves"]:
        print(x["move"]["name"])

    # part 3.1 without a loop
    print("There are " + str(len(pokeapi["game_indices"])))
    
    # part 3.2 with a loop
    count = 0
    for x in pokeapi["game_indices"]:
        count += 1
    print("There are " + str(count))
main()

