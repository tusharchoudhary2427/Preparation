# File -> A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

# File Operations
f = open("file.txt")
data = f.read() # read the content of the file
print(data)

# Write content to the file
str = "even a talking dog and a homicidal baby can't distract from the fact that everyone's still somehow dumber than Peter"
f = open("newfile.txt", "w")
f.write(str) # write the content to the file
f.close()

# Read and write content to the file at the same time
f = open("file2.txt")
line1 = f.readline()
print(line1, type(line1)) 

line2 = f.readline() 
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline() # The readline() function is used to read the content of the file line by line.
print(line4, type(line4))
f.close()


str = "Suprise mf"
f = open("file.txt", "a") 
f.write(str)
f.close()

# Using with statement to open the file
with open("file2.txt") as f: 
    print(f.read())

