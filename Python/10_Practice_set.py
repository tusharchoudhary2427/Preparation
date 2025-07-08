''' Ques 1 -> Create a class “Programmer” for storing information of few programmers working at Microsoft.'''

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.pincode = pincode
        self.salary = salary
T = Programmer("Tushar", 1000000, 123456)
print(f"Name: {T.name}, Salary: {T.salary}, Pincode: {T.pincode}, Company: {T.company}")

R = Programmer("Rahul", 1200000, 654321)
print(f"Name: {R.name}, Salary: {R.salary}, Pincode: {R.pincode}, Company: {R.company}")


''' Ques 2 -> Write a class “Calculator” capable of finding square, cube and square root of a number.'''

class Calculator:
    def __init__(self, n) :
        self.n = n 
    def square(self):
        print(f"Square is {self.n ** 2}")
    def cube(self):
        print(f"Cube is {self.n ** 3}")
    def square_root(self):
        print(f"Square root is {self.n ** 1/2}")
      
a = Calculator(4)
a.square()
a.cube()
a.square_root()

''' Ques 3 -> Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?'''

class Demo:
    a = 5

d = Demo()
print(d.a) # Prints the class attribute a, because instance attribute is not present

d.a = 0 # Instance attribute is set

print(d.a)  # This will print 0, as the instance attribute takes precedence over the class attribute

print(Demo.a)  # This will still print 5, as the class attribute is not changed

''' Ques 4 -> Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.'''

from random import randint
class Train:
    def __init__(self, train_number):
        self.train_number = train_number
        
    def book(self, From, To):
        print(f"Ticket is booked in train no: {self.train_number} from {From} to {To}")

    def getStatus(self, From, To):
        print(f"Train is running on time from {From} to {To}")

    def getFare(self, From, To):
        print(f"Ticket fair is train no: {self.train_number} from {From} to {To} is {randint(500, 5000)}")

t = Train(1234567)
t.book("Delhi", "Mumbai")
t.getStatus("Delhi", "Mumbai")
t.getFare("Delhi", "Mumbai")




