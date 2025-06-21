# Ques1 Install an external module and use it to perform an operation.

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# Ques2  Write a python program to print the contents of a directory using the os module. Search online for the function which does that.  

import os
directory_path = '/'
contents = os.listdir(directory_path)
for item in contents:
    print(item)
