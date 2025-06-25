# Condtional Expression ->  

a = int(input("Enter your age:"))

if(a >= 18): 
    print("You are an adult")  

elif(a < 0):
    print("Your are entering wrong age, age can't be in negative")

elif(a == 0):
    print("Age can't be 0")

else: 
    print("You are not an adult")
    

# Realtional Operator -> 

''' ==: equals.

!=: not equals.

> =: greater than/ equal to.

< =: lesser than/ equal to. '''

# Logical Operator ->

''' and: both conditions are true.

or: one or both conditions are true.

not: opposite of the condition. '''

# Important Point -> what if there are 2 if's, then what to do?

a = int(input("Enter your age:"))

#if statement no: 1

if(a%2 == 0):       # this int is different because i does'nt have any elif or else with it
    print("Number is even") 

#if statement no: 2

if(a >= 18):
    print("You are eligible for driving license")     # this int is different because it has elif and else with it

elif(a < 0):
    print("Your are entering wrong age, age can't be in negative")

elif(a == 0):
    print("Age can't be 0")

else: 
    print("You are not eligible for driving license")






