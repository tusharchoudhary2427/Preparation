# Ques 1 -> Write a python program to display a user entered name followed by Good Afternoon using input () function. 
txt = input("Enter your name:")
print(f"Good Afternoon, {txt}")  

# Ques 2 ->  Write a program to fill in a letter template given below with name and date. 

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|>'''

print(letter.replace("<|Name|>", "Tushar").replace("<|Date|>", "27 January 2026") )

# Ques 3 -> Write a program to detect double space in a string. 

a = "Hello   World"
print(a.find("  "))

# Ques 4 -> Replace the double space from problem 3 with single spaces.

a = "Hello   World"
print(a.replace("  ", " "))

# Ques 5 -> Write a program to format the following letter using escape sequence characters. 

letter = "Dear Tushar, \n\tyour ordered is delivered. \nThanks!"
print(letter)

