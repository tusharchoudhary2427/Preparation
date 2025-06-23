# Dictionary -> Dictionary is a collection of keys-value pairs.

marks = {
    "Tushar" : 88,
    "Rahul" : 66,
    "Rohan" : 77,
    "Shubham" : 99
}

print(marks)

print(marks["Shubham"])

# Dictionary Methods

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

