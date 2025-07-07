import random

'''
1 for snake
-1 for water
0 for gun
'''

computer =  random.choice([-1, 0, 1])

youstr = input("Enter your choice: ") # user input

youDict = {"s": 1,
           "w": -1,
           "g": 0} # dictionary for user input

reverseDict = {1: "s",
          -1: "w",
           0: "g"}

you = youDict[youstr] # convert user input to number

print(f"Computer chose: {reverseDict[computer]}") # print computer choice

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You lose")

    else:
        print("Something went wrong!!!!!!")








