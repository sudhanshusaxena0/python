name="Sudhanshu Sinha"

#Print range from string
print(name[0:10])
print(name[10:15])
print(name[5:-1])

#Print range from string with steps of 2
print(name[1:-1:2])

#Reverse a String
print(name[::-1])
print(name.upper())

#Split a string into list with seperator 'h'
print(name.split('h'))

#String Formatting
print("My name is {}".format(name))
print(f"My name is {name}")

result=1222.1023054
print("The result is {r:0.5f}".format(r=result))
print(f"The result is {result:0.5f}")
age=37
print(f"{name} age is {age}")
