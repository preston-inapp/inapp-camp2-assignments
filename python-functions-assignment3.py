import random

chances = 5
score_computer = 0
score_user = 0

moves = ["rock", "paper", "scissor"]

while(chances):
    comp_move = moves[random.randint(0,2)]
    print("Available moves {}".format(moves))
    user_move = input("Your Move : ")
    print("Computer's Move : {}".format(comp_move))
    if(user_move=="rock"):
        if(comp_move=="paper"):
            score_computer = score_computer + 1
        if(comp_move=="scissor"):
            score_user = score_user + 1
    if(user_move=="paper"):
        if(comp_move=="rock"):
            score_user = score_user + 1
        if(comp_move=="scissor"):
            score_computer = score_computer + 1
    if(user_move=="scissor"):
        if(comp_move=="rock"):
            score_computer = score_computer + 1
        if(comp_move=="paper"):
            score_user = score_user + 1
    print("Current score | Computer : {} | User : {}".format(score_computer, score_user))
    chances = chances - 1

if(score_computer > score_user):
    print("Computer Won")
elif(score_computer < score_user):
    print("You Won")
else:
    print("It is a tie")