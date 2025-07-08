# Object Oriented Programming (OOP) -> It is a programming paradigm that uses objects and classes to structure the code. It allows for encapsulation, inheritance, and polymorphism.

# Class -> A class is a blueprint for creating object.

class employee: 
    name = "Tushar" 
    designation = "Data Engineer" # This is a class attribute
    salary = 850000

# Object -> t is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.


tushar = employee() # Here tushar is instance attribute, and the class employee in allocated in it
print(f"Employee Name: {tushar.name}, Job Role: {tushar.designation}, Salary: {tushar.salary}") 

tushar = employee()
tushar.designation = "Software Engineer"
print(f"Job Role: {tushar.designation}") # It will print the Instance attributes, as take preference over class attributes. 


# Self Parameter -> self refers to the instance of the class. It is like a label to the current object and it helps the class know which object is calling the function or using the variables.

class employee:
    name = "Rahul"
    language = "Python"
    salary = 700000 

    def getinfo(self): # This is a method of the class employee, it uses self parameter to access the instance attributes
        print(f"His Name is {self.name}, the language on which he's working is: {self.language} and his salary is: {self.salary}")

Rahul = employee()
Rahul.language = "Core Java"
Rahul.getinfo() # This will call the getinfo method and print the instance attributes of Rahul


# Static Method -> Sometimes we need a function that does not use the self-parameter. We can define a static method 

class employee:
    name = "Rahul"
    language = "Python"
    salary = 700000 

    @staticmethod # This decorator is used to define a static method
    def greet(): 
        print("Hello Good Morning") 

    def getinfo(self):
        print(f"His Name is {self.name}, the language on which he's working is: {self.language} and his salary is: {self.salary}")

Rahul = employee()
Rahul.greet() # This will call the static method greet
Rahul.language = "Core Java"
Rahul.getinfo() 

# Constructor -> A constructor is a special method that is called when an object is created. It is used to initialize the instance attributes of the class. It is defined using the __init__ method.

class employee:
    language = "Python"
    salary = 700000

    def __init__(self): # Dunder method which is automatically called when an object is created
        print("Rahul is a Data Engineer")

    def getinfo(self):
        print(f"The language on which he's working is: {self.language} and his salary is: {self.salary}")

Rahul = employee()
Rahul.language = "Core Java"
Rahul.getinfo() 

    

    
