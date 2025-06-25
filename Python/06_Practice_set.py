# Ques1 -> Write a program to find the greatest of four numbers entered by the user?

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if(a>b and a>c and a>d):
    print("Greatest Number:", a)

elif(b>a and b>c and b>d):
    print("Greatest Number:", b)

elif(c>a and c>b and c>d):
    print("Greatest Number:", c)

elif(d>a and d>b and d>c):
    print("Greatest Number:", d)



# Ques2 -> Write a program to find out whether a student has passed or failed if it requires atotal of 40% and at least 33% in each subject to pass. Assume 3 subjects andtake marks as an input from the user?

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are pass in this subject", total_percentage)

else:
    ("You are failed, try again next year", total_percentage)



# Ques3 -> A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a programto detect these spams?

cmt1 = "Make a lot of money",
cmt2 = "buy now",
cmt3 = "subscribe this",
cmt4 = "click this"

message = input("Enter your comment: ") # input from user

if ((cmt1 in message) or (cmt2 in message) or (cmt3 in message) or (cmt4 in message)): # check if any of the spam comments are in the message
    
    print("This is a spam comment") # if any of the spam comments are found, print that it is a spam comment

else:
    print("This is not a spam comment") # if none of the spam comments are found, print that it is not a spam comment



# Ques4 -> Write a program to find whether a given username contains less than 10 characters or not

username = input("Enter your username: ")

if (len(username) >= 10):
    print("It contains more than 10 characters")

else :
    print("It contains less than 10 characters")



# Ques5 -> Write a program which finds out whether a given name is present in a list or not.

l = ["Tushar", "Rahul", "Rohit", "Mohit", "Amit"]
name = input("Enter your name: ") # input from user

if (name in l): # check if the name is in the list
    print("Your name is present in the list") 

else: # if the name is not found in the list
    print("Your name is not present in the list") 