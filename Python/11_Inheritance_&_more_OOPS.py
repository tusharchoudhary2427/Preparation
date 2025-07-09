'''Inheritance -> It is a way to form new classes from an existing class. The new class is called the child class and the existing class is called the parent class. The child class inherits the attributes and methods of the parent class.'''

class Employee:
    name = "Tushar"
    company = "Google"
    def show(self):
        print(f"The name of the employee is {self.name} and his company is {self.company}")


# '''class Programmer:
#      company = "Microsoft"
#      def show(self):
#          print(f"The name of the employee is {self.name} and his salary is {self.salary}")
#          def showlanguage(self):
#              print(f"The name is {self.name} is good with {self.language}")'''

'''The above code is not using inheritance.''' 

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder): # Using inheritance to create a Programmer class that inherits from Employee
    company = "Microsoft"
    def showlanguage(self):
        print(f"The name is {self.name} and is good with {self.language} language")

a = Employee()
b = Programmer() 


b.show()  # This will call the show method of Employee class
b.printLanguage()  # This will call the printLanguage method of Coder class
b.showlanguage()  # This will call the showlanguage method of Programmer class

'''The above code is using multiple inheritance'''

'''Multilevel inheritance -> It is a type of inheritance where a class inherits from another class which is already inherited by another class.'''

class employee:
    a = 1

class programmer(employee):
    b = 2

class coder(programmer):
    c = 3

o = employee()
print(o.a)  # This will print 1, as a is an attribute of employee class

o = programmer()
print(o.a, o.b)  # This will print 1, as a is inherited from employee class

o = coder()
print(o.a, o.b, o.c)  # This will print 1, 2, 3, as a is inherited from employee class and b is inherited from programmer class 


'''Super() function -> It is used to call the parent class method from the child class.'''

class employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class coder(programmer):
    def __init__(self):
        super().__init__()  # This will call the constructor of Programmer class
        print("Constructor of Coder")
    c = 3

o = coder()  

'''@classmethod -> It is used to access a class directly inside a class method.'''

class Employee:
    company = "Google"
    
    @classmethod
    def show(cls):
        print(f"The company is {cls.company}")

e = Employee()
e.company = "Microsoft"  # This will not change the class attribute company, as it is an instance attribute
e.show()  # This will call the show method of Employee class 

'''@property -> It is used to create a property of a class. It is used to access the instance attribute as a property. '''



'''Operator Overloading -> It is a way to define the behavior of operators for user-defined classes. It allows us to use operators like +, -, *, /, etc. with user-defined classes.'''

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(5)
m = Number(10)

print(n + m)  # This will give an error, as + operator is not defined for Number class