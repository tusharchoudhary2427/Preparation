# Ques 1 -> Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2D Vector: ({self.i}i, {self.j}j)")  

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
       super().__init__(i,j)  # Call the constructor of TwoDVector
       self.k = k

    def show(self):
        print(f"3D Vector: ({self.i}i, {self.j}k, {self.k}k)")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show()

# Ques 2 ->  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’
    
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")

d = Dog()
d.bark()  

# Ques 3 -> Create a class ‘Employee’ and add salary and increment properties to it. After that Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    salary = 250
    increment = 100
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1) *100  # This will set the increment based on the salary


e = Employee()

e.salaryAfterIncrement= 275  # This will set the increment to 10%
print(e.increment)  

#print(f"Initial Salary: {e.salary} and Increment: {e.increment} and the final salary: {e.salary + e.increment}")

# Ques 4 -> Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r                                                      # self.r and self.i are variables that belong to the object  (right side r is the value the user gives and left side self.r is the variable that belongs to the object)
        self.i = i
    
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self): # It tells Python how to represent your object as a string when you use print() or str().
        return f"{self.r} + {self.i}"
    

c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 + c2)  # This will call the __add__ method and print the result of addition

# Ques 5 -> Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)  # This will call the __add__ method and print the result of addition
print(v1 * v2)  # This will call the __mul__ method and print the result of dot product

print(v1 + v3) # This will call the __add__ method and print the result of addition
print(v1 * v3) # This will call the __mul__ method and print the result of dot product
