# WALRUS OPERATOR -> It allows you to assign a value to a variable within an expression, rather than as a separate statement.

# Example 1: Using the walrus operator to assign a value within an if/else statement
if (n := len([1,2,3,4,5])) > 3:
    print(f"The length of the list is {n}, which is greater than 3.")
else:
    print(f"The length of the list is {n}, which is not greater than 3.")

# TYPES DEFINITIONS -> In this hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

age: int = 23
def greet(name: str) -> str:
    return f"His Name is {name} and his age is {age}"

print(greet("Tushar"))  # Output: Hello, Alice!

# ADVANCED TYPE HINTS -> Python supports advanced type hints that allow for more complex data structures and types.

from typing import List, Dict, Tuple, Union

numbers: list[int] = [1, 2, 3, 4, 5]

person: tuple[str, int] = ("Tushar", 23)

marks: dict[str, int] = {"Math": 90, "Science": 85}

indentifier: Union[int, str] = "Tushar123"

print(f"His Name is {person[0]} and his age is {person[1]}, his marks are {marks['Math']} in Math and {marks['Science']} in Science, and his unique id is {indentifier}.")

# MATCH CASE -> provides a way to execute different blocks of code based on the value of a single variable or expression

def designationwithsalary(designation: str, salary: int):
    match designation: # we can't write salary: int here, as match case doesn't support type hints and also against a single string, which won’t work correctly

        case "Software Engineer":
            print(f"Designation: {designation}, Salary: {salary}")

        case "Data Scientist":
            print(f"Designation: {designation}, Salary: {salary}")

        case "Product Manager":
            print(f"Designation: {designation}, Salary: {salary}")

        case _:
            print("Unknown designation")

designationwithsalary("Software Engineer", 100000)
   
# DICTIONARY MERGE & UPDATE OPERATORS -> It is a new operators, | and |= allow for merging and updating dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2  
print(merged_dict) 

# with the update operator

# with (
# open('file.txt') as f1,
# open('file2.txt') as f2
# ):

#     content1 = f1.read()
#     content2 = f2.read()

# EXCEPTION HANDLING -> It is the code that handles the exception is written in the except clause. It can be handled using a try statement.

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

# RAISING EXCEPTIONS -> we can raise exceptions using the raise statement. This is useful when we want to enforce certain conditions in our code.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")

else:
    print(f"The result of {a} divided by {b} is {a / b}")


# TRY WITH ELSE -> It is used to execute a block of code if no exceptions are raised in the try block.

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("No exceptions were raised, so this block is executed.")

# TRY WITH FINALLY -> It is used to execute a block of code regardless of whether an exception was raised or not.

def main():

    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print(e)  # Executed on error
        return
    
    finally:
        print("Hey I am inside finally block")  # Always executed

main()









