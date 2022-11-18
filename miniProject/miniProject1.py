#!/usr/bin/env python3
import sys
# What is your Zodiac sign?
def yearToZodiac():
    # create a dictionary to contain Chinese Zodiac
    zodiac = {  0:"Rat", 
                1: "Ox", 
                2:"Tiger", 
                3:"Hare", 
                4:"Dragon", 
                5:"Snake", 
                6:"Horse", 
                7:"Sheep", 
                8:"Monkey", 
                9:"Rooster", 
                10:"Dog", 
                11:"Pig"}

    # print a question
    print("Do you want to know your or someone's Chinese Zodiac sign?")
    
    # set a condition
    condition = True
    
    while condition:

        # get a year from the user
        year = input("Please type the year you or someone were/was born(example: 2020): ")

        # check user input validation
        if len(year) == 4 and year.isdigit():
            # convert string to integer
            year = int(year)
        else:
            continue
        
        # display the result
        print(str(year) + " is a year of " + zodiac[(year -2020)%12])
        print()

        # ask user for keepgooing or not
        condition = keepGoing()
 
def zodiacToYear():
    year = {"Rat": 0, 
            "Ox": 1, 
            "Tiger":2, 
            "Hare":3, 
            "Dragon":4, 
            "Snake":5, 
            "Horse":6, 
            "Sheep":7, 
            "Monkey":8, 
            "Rooster":9, 
            "Dog":10, 
            "Pig":11}
    zodiac = ["Rat", "Ox", "Tiger","Hare","Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster","Dog", "Pig"]

    # set a condition
    condition = True

    while condition:
        # collect years
        years = []

        # question
        print(zodiac)
        userInput = input("Enter one of Chinese Zodiac: ").capitalize()
        # check user input validation
        if userInput not in zodiac:
            continue
 
        # display the result
        
        for x in range(1900, 2022):
            if (x - 2020) % 12 == year[userInput]:
                years.append(x)

        print("Years of " + userInput + ":" + str(years))
        print()
        
        # ask user for keepgooing or not
        condition = keepGoing()

def keepGoing():
    condition = True
    # ask user for keepgooing or not
    userInput = input("Do you want to do it again?(y/n): ").lower()

    if userInput == "y":
        condition = True
    else:
        condition = False
        menu = input("Do you want to go back to main menu or quit?(y/q): ").lower()
        if menu == "y":
            main()
        else:
            sys.exit()

    return condition

def main():

    condition = True
    while condition:
        print("What do you want to check?")
        print("\t1. Enter a year to check your Chinese Zodiac")
        print("\t2. Enter a Chinese Zodiac to check which years correlate to which Chinese Zodiac")
        num = input(">")
        if num.isdigit():
            if num == "1":
                yearToZodiac()
            elif num == "2":
                zodiacToYear()
            else:
                continue
        else:
            continue


if __name__ == "__main__":
    main()