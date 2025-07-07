'''
1 for snake
-1 for water
0 for gun
'''

computer = -1 # water

youstr = input("Enter your choice: ") # user input

youDict = {"s": 1,
           "w": -1,
           "g": 0} # dictionary for user input

you = youDict[youstr] # convert user input to number

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




