# Ques 1 -> Write a program to input name, marks and phone number of a student and format it using the format function like below: “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter the student's name: ")
marks = int(input("Enter the student's marks: "))
phone_number = int(input("Enter the student's phone number: "))

s = (f"The name of the student is {name}, his marks are {marks} and phone number is {phone_number}".format(name, marks, phone_number))

print(s)    

# Ques 2 -> A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

l = [str(7 * i) for i in range(1, 11)]

s = "\n".join(l)
print(s)

# Ques 3 -> Write a program to filter a list of numbers which are divisible by 5.

def divisible_by_5(n):
    if n % 5 == 0:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
filtered_list = list(filter(divisible_by_5, l))

print(filtered_list)

# Ques 4 -> Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def greater(a, b):
    if a > b:
        return a
    else:
        return b
    
print(reduce(greater, l))  # This will return the maximum number in the list l