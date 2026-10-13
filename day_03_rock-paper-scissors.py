import random

choices= ["rock", "paper", "scissors"]

print ("let's play!rock paper scissors")
while True:

    choose= input("choose : rock/paper/scissor/quit: ").lower()

    if choose == "quit":
     print ("thank you for playing!")
     break
    if choose not in choices:
     print ("enter valid input")
     continue

    comp_choice = random.choice(choices)
    print (f'your choice is {choose}')
    print (f'computer choice is {comp_choice}')

    if comp_choice==choose:
        print("it's a tie")
    elif (
        (choose== "rock" and comp_choice == "scissors")
        or (choose== "paper" and comp_choice == "rock")
        or (choose== "scissors"and comp_choice== "paper")):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
    
