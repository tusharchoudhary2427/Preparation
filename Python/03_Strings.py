# String -> It is a data type that represents a sequence of characters, such as a word or a sentence.Strings are enclosed in quotes, either single quotes or double quotes.

name = "John"  
print(name)  

# String Slicing

name = 'Tushar'
nameshort = name[2:5] # positive indexing
print(nameshort)


name = 'Justin'
nameshort = name[-5:-2] # negative indexing
print(nameshort)

# Silicing with skip value
name = 'Tushar'
name = name[1:5] 
print(name)

# Functions in Strings

name = "tushar choudhary"

print(len(name)) # returns the length of the string

print(name.endswith("ar")) # returns True if the string ends with 'ar', otherwise False

print(name.startswith("Tu")) # returns True if the string starts with 'Tu', otherwise False

print(name.capitalize()) # returns the string with the first character capitalized and the rest in lowercase

print(name.upper()) # returns the string in uppercase

print(name.lower()) # returns the string in lowercase

print(name.title()) # returns the string with the first character of each word capitalized

print(name.find("h")) # returns the index of the first occurrence of 'h' in the string

print(name.replace("choudhary", "choudhary123")) # returns the string with 'choudhary' replaced with 'choudhary123'

# Escape Sequences -> To insert characters that are illegal in a string, use an escape character.

txt = "joined Tinder to find a \nnew heist partner." # \n is the escape sequence for a new line
print(txt)

txt = "Winter is coming' \tevery time AC was on" # \t is the escape sequence for a tab
print(txt)

txt = "mistook \"Demogorgon\" for their ex"
print(txt)

txt = 'tried cooking Maggi like \'meth\' ' #  is used for single quotes
print(txt)
