# Ques 1 -> Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open('1.txt', 'r') as f1:
        print(f1.read())
except FileNotFoundError:
    print("1.txt not found.")

try:
    with open('2.txt', 'r') as f2:
        print(f2.read())
except FileNotFoundError:
    print("2.txt not found.")

try:
    with open('3.txt', 'r') as f3: 
        print(f3.read())
except FileNotFoundError:
    print("3.txt not found.") 

print("Program completed.")

# Ques 2 -> Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:  
        print(item)

# Ques 3 -> Write a list comprehension to print a list which contains the multiplication table of a user entered number

n = int(input("Enter a number: "))
multiplication_table = [n * i for i in range(1, 11)]
print(f"Multiplication table of {n}: {multiplication_table}")

# Ques 4 -> Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))

    print(f"{a} divided by {b} is {a / b}")

except ZeroDivisionError as v:
    print("Infinite (Division by zero is not allowed)")

