#!/usr/bin/env python3

farms1 = [{"name": "NE Farm", 
            "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", 
             "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", 
             "agriculture": ["chickens", "carrots", "celery"]}]

farms2 = [{"name": "Southwest Farm", 
            "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", 
             "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", 
             "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", 
             "agriculture": ["pigs", "chickens", "llamas"]}]
       
# what are the vegs and fruit objects?
# tuples!
vegs = ("carrots", "celery")
fruit = ("bananas", "apples", "oranges")

def animal(farms, farmname):
    animals = []
    for x in farms:
        if x["name"].lower() == farmname.lower():
            for y in x["agriculture"]:
                if y not in vegs and y not in fruit:
                    animals.append(y)
    return animals

def main():
    condition = True
    while condition:
        farms = input("Choose a farms data (farms1 or farms2): ")
        if farms == "farms1":
            farms = farms1
            condition = False
        elif farms == "farms2":
            farms = farms2
            condition = False
        else:
            continue
    listOfFarms = []
    print("There are ", end="")
    for x in range(len(farms)):
        listOfFarms.append(farms[x]["name"])
        print(farms[x]["name"], end=", ")
    
    
    farmname = input("please choose a farmname: ")
    while farmname not in listOfFarms:
        farmname = input("plase choose a correct farmname: ")
    print(animal(farms, farmname))

if __name__ == "__main__":
    main()






















