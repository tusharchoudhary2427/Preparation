'''Dictionary -> Dictionary is a collection of keys-value pairs.'''

marks = {
    "Tushar" : 88,
    "Rahul" : 66,
    "Rohan" : 77,
    "Shubham" : 99
}

print(marks)

print(marks["Shubham"])

'''Dictionary Methods'''

print(marks.items()) # Returns a list of dictionary's key-value tuple pairs

print(marks.keys()) # Returns a list of dictionary's keys

print(marks.values()) # Returns a list of dictionary's values

marks.update({"Shubham": 88}) # Updates the value of the key "Shubham" to 88
print(marks)

print(marks.get("Rahul")) # Returns the value of the key "Rahul" if it exists in the dictionary

'''Important point ->  print(marks.get("Rahul2")) prints none
                      print(marks["Rahul2"]) return an error '''

marks.pop("Rohan")
print(marks) # Removes the key-value pair with key "Rohan" from the dictionary

''' Sets -> A set is an unordered collection of non-repetitive elements.It is defined by curly brackets {} and elements are separated by comma.'''

set = {1,2,3}
print(set) # Prints the set of elements
print(type(set)) # Prints the type of the set

'''e = set()
print(type(e))  Prints an empty set'''

b = {1,1,1,3,4,5,67,55,69,69,44}
print(b) # Prints the set of elements, duplicates are removed, unordered collection
print(sorted(b))

'''Sets Methods'''

s = {3, 89, 17, 56, 24, 77, 11}

s.add(444) # Adds an element to the set
print(s)

s.remove(89) # Removes an element from the set
print(s) 

s.pop()
print(s) # Removes an element from the set, if the element is not present it raises an error 

'''Set Union and Intersection'''

s1 = {22, 44, 67, 90}
s2 = {44, 45, 18 , 22}

print(s1.union(s2)) # Returns a new set with elements from both sets

print(s1.intersection(s2)) # Returns a new set with elements common to both sets

print(s1.difference(s2)) # Returns a new set with elements in s1 but not in s2

