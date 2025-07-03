# Ques 1 -> Write a program to print multiplication table of a given number using for loop

n = int(input("Enter a number:  "))

for i in range(1, 11): 
    print(f"{n} * {i} = {n * i}")

# Ques 2 ->  Write a program to print multiplication table of a given number using for loop

n = int(input("Enter a number:  "))

i = 1
while(i<11):
    print(f"{n} * {i} = {n * i}")
    i += 1

# Ques 3 -> Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Tushar", "Sonam", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print(f"Hello, {name}")

# Ques 4 -> Write a program to find whether a given number is prime or not.

n = int(input("Enter a number:  "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")

# Ques 5 -> Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number:  "))
i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1
print(sum)

# Ques 6 -> Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number:  "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print(fact)



