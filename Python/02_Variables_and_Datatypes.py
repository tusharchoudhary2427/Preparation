#variables

a = 1 # => a is variable which contain value 1

b = 2 # => b is variable which contain value 2

print(a + b) # => print the sum of a and b

# operators

# 1. Arithmetic operators -> +, -, *, /, % (modulus), etc.

a = 10
b = 2
c = a + b 
print(c)

# 2. Comparison operators -> ==, !=, >

a = 10
b = 20
print(a > b)

# 3. Logical operators -> and, or, not

#i)
a = True
b = False
print(a and b)

#ii)
a = True
b = False
print(a or b)

# 4. Assignment operators -> =, +=, -=, *=, /=, %=, etc.

a = 4-2 # => Assign 4-2 in a
print(a) 
b = 6
b += 3 # => Increment the value of b by 3 and then assign it to b
print(b) 

# type function
a = 10
print(type(a)) # => print the type of a

x = 31.2
print(type(x)) 

# type casting

a = "31.69"
b = float(a)

type (b)

# input function
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Number a is:", a)
print("Number b is:", b)
print("Sum:", a+b)
