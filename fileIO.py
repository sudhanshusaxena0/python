myfile=open("myfile.txt")
print(myfile.read())
#Below print statement will not print again as the cursor is on end of file
print(myfile.read())
#seek function is used to bring the curson back to 0 position to read from start of file
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
contents=myfile.read()
print(contents)

#read file lines in a list
myfile.seek(0)
contents=myfile.readlines()
print(contents)
