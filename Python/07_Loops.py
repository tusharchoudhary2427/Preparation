# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how! The computer will repeat the instructions as long as the condition is true.



'''While loops''' # While loops are similar to for loops, but they repeat the instructions as long as the condition is true.

i = 1
while (i < 10):
    print(i)
    i += 1


# Quick Quiz: Write a program to print the content of a list using while loops

l = [1, "Tushar", False, "Hello", "Amit", "Rahul"]

i = 0

while (i< len(l)):
    print(l[i])
    i += 1

'''For loops''' # For loops are used to iterate over a sequence (like a list, tuple, dictionary, set , or string) and perform a specified action for each item in the sequence. 

for i in range(1,4):
    print(i)

# step_size 

for i in range(0, 51, 5): # This will print numbers from 0 to 51 with a step size of 5
    print (i)

# for loop iterate 

# for loop with lists
l = [1, 4, 6, 89, 456, 67]  
for i in l:
    print(i)

# for loop with Tuples
t = (44, 56, 69, 30)
for i in sorted(t):
    print(i)

# for loop with dictionaries
d = {"apple": 10, "banana": 5, "orange": 8}

for key in d:
    print(key)

# for loop with String
s = "Hello, World!"
for i in s:
    print(i)


# for loop with else
l = [1, 4, 6, 89, 456, 67]
for i in l:
    print(i)


else:
    print("done") # This will print "done" if the loop completes normally (i.e., without a break statement)


# for loop with break statement
i = 1
for i in range(100):
    if(i == 35):
        break # This will stop the loop when i is 35
    print(i)


# for loop with continue statement
i = 1
for i in range(100):
    if(i == 35) or (i == 50):
        continue # This will skip the print statement when i is 35
    print(i)

# pass statement -> It instruct to do nothing

i = 0
for i in range(44):
    pass

i = 1
while(i < 45):
    print(i)
    i = i + 1


