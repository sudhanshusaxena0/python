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

#open file with path on windows
#In linux we define path as "/root/example/all.csv"
myfile1=open("C:\\python\\cities.csv")
print(myfile1.read())
myfile1.close()

# To auto close the file use below method
with open("myfile.txt") as my_file2:
    contents=my_file2.read()
    print(contents)

print(contents)

with open("myfile1.txt",mode="w+") as my_file3:
    my_file3.write("\nNew line")
    my_file3.seek(0)
    print(my_file3.read())

with open("myfile2.txt",mode="a") as my_file3:
    my_file3.write("\nNew line")

with open("myfile2.txt",mode='r') as my_file4:
    print(my_file4.read())
