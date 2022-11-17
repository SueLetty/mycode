#i!/usr/bin/env python3

condition = True
while condition:

    # save a user's input to the variable char_name 
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)").capitalize()

    # save a user's input to the variable char_stat 
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)").lower()

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

    "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }
    if char_stat == "real name":
        print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}")
    else:
        print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

    check = input("Do you want to look up another charactor? (y/n)").lower()
    if check == "y":
        condition = True
    else:
        condition = False










