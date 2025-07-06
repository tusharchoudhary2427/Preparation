# Ques 1 -> Write a program to read the text from a given file ‘sarcastic.txt’ and find out whether it contains the word ‘genius’.

with open("sarcastic.txt") as f:
    content = f.read()
    if 'genius' in content:
        print("'genius' is present in the file.")
    else :
        print("'genius' is not present in the file.")

# Ques 2 -> A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 

word = "Donkey"

with open("filedonke.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("filedonke.txt", "w") as f:
    f.write(contentNew)

