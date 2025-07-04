# Ques 1 -> Write a program using functions to find greatest of three numbers

a = 35
b = 45
c = 44

def greatest(a, b, c):
    if (a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
    else:
        return "All numbers are equal"
print(greatest(a,b,c))

# Ques 2 -> Write a python program using function to convert Celsius to Fahrenheit.(c/5 = (f-32)/9)

def f_to_c(f):
    celsius = 5 * (f - 32) / 9
    return round(celsius, 2)

f = float(input("Enter Temperature in °F: "))
print(str(f_to_c(f)) + "°C")

# Ques 3 -> Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(n) = 1 + 2 + 3 + 4.......n
sum(n) = sum(n-1) + n

'''
def sum(n):
    if(n == 1):
        return 1
    return sum(n - 1) + n

print(sum(5))


# Ques 4 -> Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54
n = int(input("Enter the Value in inches:  "))
print(inch_to_cm(n))

# Ques 5 -> Write a python function to remove a given word from a list ad strip it at the same time.

def remove_word(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
    return n


l = ["Tushar", "Rohan", "Aryan", "Karan", "Vicky", "an"]

print(remove_word(l,"an"))
