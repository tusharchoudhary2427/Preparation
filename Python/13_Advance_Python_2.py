# LAMBDA FUNCTIONS -> Function created using an expression using ‘lambda’ keyword, which can take any number of arguments but can only have one expression. It is used for creating small anonymous functions.

'''Quick example: write a square function using lambda'''

square = lambda x: x * x
print(square(5))

# JOIN METHOD (STRINGS) -> It is used to join a list of strings into a single string with a specified separator.

a = ["Tushar", "Rahul", "Rohan"]

final = " and ".join(a)
print(final) 

# FORMAT METHOD (STRINGS) -> It is used to format strings by replacing placeholders with values.

name = "Tushar"
age = 23    
formatted_string = "His name is {} and his age is {}".format(name, age)
print(formatted_string)

# MAP, FILTER & REDUCE -> These are higher-order functions that allow you to apply a function to a sequence of elements.

'''MAP -> It applies a function to all items in an input list and returns a new list with the results.'''

l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqList = map(square, l)  # This will apply the square function to all items in the list l
print(list(sqList)) 

'''FILTER -> It filters the items in a list based on a condition and returns a new list with the items that satisfy the condition'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(list(filter(even, l)))  # This will filter the even numbers from the list l

# REDUCE -> Reduce applies a rolling computation to sequential pair of elements. 

from functools import reduce
l = [1, 2, 3, 4, 5]
def sum(a, b):
    return a + b

mul = lambda a, b: a * b

print(reduce(sum, l))  # This will return the sum of all elements in the list l
print(reduce(mul, l))  # This will return the product of all elements in the list l
