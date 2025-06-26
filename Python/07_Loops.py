# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how! The computer will repeat the instructions as long as the condition is true.

for i in range(1, 6): # This will repeat the instructions 5 times (from 1 to 5)
    print(i) 

'''While loops''' # While loops are similar to for loops, but they repeat the instructions as long as the condition is true.

i = 1
while (i < 10):
    print(i)
    i += 1


# Quick Quiz: Write a program to print the content of a list using while loops

l = [10, "Tushar", False, "Rohan", "Maverick", "Rohit", True] 

i = 0
while (i<len(l)):
    print(l[i])
    i =+ 1
