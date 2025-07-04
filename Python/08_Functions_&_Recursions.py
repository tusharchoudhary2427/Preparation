# Functions -> A function is a block of code which only runs when it is called.  A function is a group of statements performing a specific task.

def avg(): # This is a function definition.
    
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    average = (a + b + c) / 3
    print(average)

avg() # This is a function call. 

# Quick Quiz -> Write a program to greet a user with “Good day” using functions

def goodDay():
    name = input("Enter your name: ")
    print("Good day, " + name)
    
goodDay()

# Types of Functions -> There are two types of functions in Python: Built-in functions and User-defined functions.

