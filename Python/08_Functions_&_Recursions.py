# Functions -> A function is a block of code which only runs when it is called.  A function is a group of statements performing a specific task.

def avg(): # This is a function definition.
    
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    average = (a + b + c) / 3
    print(average)

avg() # This is a function call. 



#FUNCTIONS WITH ARGUMENTS -> Write a program to greet a user with “Good day” using functions

def goodDay(name, ending):
    print("Good day, " + name)
    print(ending)
    return "done"

a = goodDay("Tushar", "Thanks")
print (a)

# DEFAULT PARAMETER VALUE -> If a function has a parameter with a default value, you can call the function without passing a value for that parameter.

def greet(name = "stranger"):
    greet()
    greet("harry") 


# RECURSION -> Recursion is a function which calls itself

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter Your Number: "))
print(f"The factorial of this number is: {factorial(n)}")
