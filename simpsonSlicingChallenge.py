#!/usr/bin/env python3

def printSentence0():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

    # Display "My eyes! The goggles do nothing!" from the challenge
    result = "My " + challenge[2][1] + "! The " + challenge[2][0] + " do "+challenge[-1] +"!"
    return result

# Display "My eyes! The goggles do nothing!" from trial
def printSentence1():

    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

    result = "My " + trial[2]["goggles"] + "! The " + trial[2]["eyes"] + " do " +trial[-1] +"!"
    return result

# Display "My eyes! The goggles do nothing!
def printSentence2():

    nightmare= [{"slappy": "a", 
                    "text": "b", 
                    "kumquat": "goggles", 
                    "user":{"awesome": "c", 
                                "name": {"first": "eyes", 
                                            "last": "toes"}},
                    "banana": 15, 
                    "d": "nothing"}]

    # Display "My eyes! The googles do nothing!
    result = "My " + nightmare[0]["user"]["name"]["first"] + "! The " + nightmare[0]["kumquat"] + " do " +nightmare[0]["d"] +"!"
    return result

print(printSentence0())
print(printSentence1())
print(printSentence2())
