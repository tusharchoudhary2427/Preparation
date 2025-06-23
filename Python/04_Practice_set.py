# Ques 1 -> Write a program to store seven fruits in a list entered by the user. 

fruits = []
f1 = input("Enter fruit Name: ")
fruits.append(f1)
f2 = input("Enter fruit Name: ")
fruits.append(f2)
f3 = input("Enter fruit Name: ")
fruits.append(f3)
f4 = input("Enter fruit Name: ")
fruits.append(f4)
f5 = input("Enter fruit Name: ")
fruits.append(f5)
f6 = input("Enter fruit Name: ")
fruits.append(f6)
f7 = input("Enter fruit Name: ")
fruits.append(f7)

print(fruits)

# Ques 2 ->  Write a program to accept marks of 6 students and display them in a sorted manner. 

marks = []
m1 = int(input("Enter you marks = "))
marks.append(m1)
m2 = int(input("Enter you marks = "))
marks.append(m2)
m3 = int(input("Enter you marks = "))
marks.append(m3)
m4 = int(input("Enter you marks = "))
marks.append(m4)
m5 = int(input("Enter you marks = "))
marks.append(m5)
m6 = int(input("Enter you marks = "))
marks.append(m6)

marks.sort()
print(marks)

# Ques 3 -> Write a program to sum a list with 4 numbers. 

a = [22,44,66,88]

print(sum(a))

# Ques 4 -> Write a program to count the number of zeros

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))



