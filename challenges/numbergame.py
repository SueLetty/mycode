#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num= random.randint(1,100)
    guess = -1 # declare the variable
    rounds= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit() and 1 <= int(guess) <= 100: # added second condition
           guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1 # added =

        elif guess < num:
            print("Too low!")
            rounds += 1 # added =

        else:
            print("Correct!")
main() # called function
