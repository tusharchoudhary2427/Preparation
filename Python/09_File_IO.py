# File -> A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.


f = open("file.txt")
data = f.read()
print(data)
f.close()