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
         
vegs = ("carrots", "celery")
fruit = ("bananas", "apples", "oranges")

def animal(farms, farmname):
    animals = []
    for x in farms:
        if x["name"] == farmname:
            for y in x["agriculture"]:
                if y not in vegs and y not in fruit:
                    animals.append(y)
    return animals

def main():

    farms = input("Choose a farms data (farms1 or farms2): ")
    print("There are ", end="")
    if farms == "farms1":
        farms = farms1
    elif farms == "farms2":
        farms = farms2
    for x in range(len(farms)):
        print(farms[x]["name"], end=", ")
    farmname = input("\nplease choose a farmname: ")
    print(animal(farms, farmname))

if __name__ == "__main__":
    main()
