# File -> A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.


f = open("file.txt")
data = f.read() # read the content of the file
print(data)



str = "even a talking dog and a homicidal baby can't distract from the fact that everyone's still somehow dumber than Peter"
f = open("newfile.txt", "w")
f.write(str) # write the content to the file
f.close()

f = open("file2.txt")
line1 = f.readline()
print(line1, type(line1)) 

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))
# In the above code, we are trying to read the content of a file.
f.close()

