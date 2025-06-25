# Ques1 -> Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "Madad": "Help",
    "Sochna":  "Think",
    "Bhool": "Forget",
    "Khush": "Happy",
    "Dhokha": "Cheated",
    "Dharm": "Religion",
}

word = input("Enter the word:")
print(words[word])

# Ques2 -> Write a program to input eight numbers from the user and display all the unique numbers (once).  

s = set()

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

n = input("Enter number: ") 
s.add(int(n)) 

print(s)

# Ques3 -> Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add("18")

print(s) # Output: {18, '18'}

# Ques4 -> Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
language = input("Enter language name: ")
d.update({name:language})

name = input("Enter friends name: ")
language = input("Enter language name: ")
d.update({name:language})

name = input("Enter friends name: ")
language = input("Enter language name: ")
d.update({name:language})

name = input("Enter friends name: ")
language = input("Enter language name: ")
d.update({name:language})

print(d)

# Ques5 -> Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Tushar", [1,2]} 
# we cannot include a list in a set 

