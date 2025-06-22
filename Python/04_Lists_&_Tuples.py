# Lists -> It is container that is used to store a set of values of any datatypes

collection = ["Apple", "Samsung", 5, 78.68, "Tushar"]
print(collection)
collection[0] = "Sony"
print(collection)

collection.append("Choudhary")
print(collection)

# Lists Methods

list1 = [1,3,5,77,2,4]

list1.sort()
print(list1) # Sorts the list in ascending order

list1.reverse()
print(list1) # Reverses the list

list1.insert(4, 6)
list1.sort()
print(list1) # Inserts a value at a specified position

list1.pop(6)
print(list1) # Removes the last element from the list

list1.remove(5)
print(list1)

# Tuples -> It is a collection of values that are ordered and immutable, it is similar to list but it is immutable.

a = (1, )
print(type(a))

# Tuple Methods
tpl1 = (1, 2, 3, 4, 5)
tpl2 = (10, 9, 8, 7, 6)
print(tpl1) 

print(tpl1.count(4)) # Counts the specified value

print(tpl1.index(3)) # Returns the index of the specified value

print(tpl1 + tpl2) # Concatenates two tuples

print(tpl2 * 2) # Repeats the tuple a specified number of times

print(4 in tpl1) # Checks if a value is present in the tuple

print(len(tpl2)) # Returns the length of the tuple