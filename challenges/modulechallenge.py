#!/usr/bin/env python3

import html

def triviaGame():
    # create a script that includes the trivia dictionary

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

    # slice and print out the trivia question and the four answers( one correct, three incorrect) from the idctionary
    question = trivia["question"]
    correct = html.unescape(trivia["correct_answer"])
    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect3 = html.unescape(trivia["incorrect_answers"][2])
    # use the html libaray to render the question/answers in the proper format


    # BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly
    print(question)
    print("A: " + correct)
    print("B: " + incorrect1)
    print("C: " + incorrect2)
    print("D: " + incorrect3)

    answer = input("Please choose a correct answer A, B, C, or D: ").capitalize()

    while True:
        if answer == "A":
            print("You got it right!")
            return
        else:
            print("try agian!")
            answer = input("Please choose a correct answer A, B, C, or D: ").capitalize()

triviaGame()
