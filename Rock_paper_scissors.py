
# Rock, Paper and Scissors Game

import random

print("WELCOME TO ROCK PAPER SCISSORS GAME!!")

i = 0

choose = ["Rock", "Paper", "Scissors"]

c_points = 0
p_points = 0

while i < 10:

    c_choose = random.choice(choose)

    p_choose = int(input("Enter:- \n"
                  "1 for Rock \n"
                  "2 for Paper \n"
                  "3 for Scissors \n"
                         ": "))

    if c_choose == "Rock" and p_choose == 1:
        print("Computer chose : Rock")
        print("Draw")
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Rock" and p_choose == 2:
        print("Computer chose: Rock")
        print("You won!")
        p_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Rock" and p_choose == 3:
        print("Computer chose: Rock")
        print("You lost!")
        c_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Paper" and p_choose == 1:
        print("Computer chose: Paper")
        print("You lost!")
        c_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Paper" and p_choose == 2:
        print("Computer chose: Paper")
        print("Draw")
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Paper" and p_choose == 3:
        print("Computer chose: Paper")
        print("You won!")
        p_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Scissors" and p_choose == 1:
        print("Computer chose: Scissors")
        print("You won!")
        p_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Scissors" and p_choose == 2:
        print("Computer chose: Scissors")
        print("You lost!")
        c_points += 1
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    elif c_choose == "Scissors" and p_choose == 3:
        print("Computer chose: Scissors")
        print("Draw")
        print("Your points: ", p_points, )
        print("Computer points: ", c_points, "\n")

    i += 1