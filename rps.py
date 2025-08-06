"""
Workflow Of Project
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""


import random

item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter Your Move = Rock,Paper,Scissor =")
computer_choice=random.choice(item_list)
print(f"User Choice={user_choice},Computer Choice={computer_choice}")
if user_choice==computer_choice :
    print("Both Chooses Same:= Match Tie")

elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper Covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print("Scissor Cuts Paper = Computer Win")
    else:
        print("Paper Covers Rock = You Win")

elif user_choice=="Scissor":
    if computer_choice=="Paper":
        print("Scissor Cuts Paper = You Win")
    else:
        print("Rock Smashes Scissor = Computer Win")       

               

