for num in range(10):
    print(num)

print("\n\n\n")
for num in range(0,10,2):
    print(num)

print("\n\n\n")
print(list(range(1,10)))

index=0
for i in "sudhanshu":
    print(f"intex {index} value is {i}")
    index+=1

print("\n\n\n")
for item in enumerate("sudhanshu"):
    print(item)

print("\n\n\n")
for index,value in enumerate("sudhanshu"):
    print(index)
    print(value)
    print("\n")

print("\n\n\n")
l1=[1,2,3,4]
l2=['a','b','c','d']
l3=l1+l2
print(l3)

print("\n\n\n")
l1=[1,2,3,4]
l2=['a','b','c','d']
l3=zip(l1,l2)
print(type(l3))

print("\n\n\n")
l1=[1,2,3,4]
l2=['a','b','c','d']
for item in zip(l1,l2):
    print(item)

print("\n\n\n")
l1=[1,2,3,4,5,6]
l2=['a','b','c','d']
for item in zip(l1,l2):
    print(item)

print("\n\n\n")
l1=[1,2,3,4,5,6]
l2=['a','b','c','d']
l3=['abc','xyz','lmn']
for item in zip(l1,l2,l3):
    print(item)

print("\n\n\n")
l1=[1,2,3,4,5,6]
l2=['a','b','c','d']
l3=list(zip(l1,l2))
print(l3)

print("\n\n\n")
l1=[1,2,3,4,5,6]
print(4 in l1)

print("\n\n\n")
l1=['a','b','c','d','e','f']
print('b' in l1)

print("\n\n\n")
l1=['a','b','c','d','e','f']
print('g' in l1)

print("\n\n\n")
s1="Sudhanshu"
print('S' in s1)

print("\n\n\n")
s1="Sudhanshu"
print('v' in s1)

print("\n\n\n")
d1={'name':'Ayush','age':'13'}
print('name' in d1)

print("\n\n\n")
d1={'name':'Ayush','age':'13'}
print('name1' in d1)

print("\n\n\n")
d1={'name':'Ayush','age':'13'}
print('name' in d1.keys())

print("\n\n\n")
d1={'name':'Ayush','age':'13'}
print('Ayush' in d1.values())

print("\n\n\n")
num=[10,20,5,30,50,40]
print(min(num))
print(max(num))

from random import shuffle
print("\n\n\n")
num=[10,20,5,30,50,40]
print(num)
l1=shuffle(num)
print(num)

from random import randint
print("\n\n\n")
print(randint(0,100))
print(randint(0,100))

print("\n\n\n")
name=input("Enter your name: ")
print(f"Name entered is {name}")

age=input("Enter your age: ")
print(type(age))
print(type(int(age)))

print("\n\n\n")
name="sudhanshu"
l1=[]
for i in name:
    l1.append(i)
print(l1)

print("\n\n\n")
name="sudhanshu"
l1=[i for i in name]
print(l1)

print("\n\n\n")
l1=[x for x in "hello how are you"]
print(l1)

print("\n\n\n")
l1=[x for x in range(0,100)]
print(l1)

print("\n\n\n")
l1=[x*2 for x in range(0,10)]
print(l1)

print("\n\n\n")
l1=[x for x in range(0,11) if x%2==0]
print(l1)

print("\n\n\n")
celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(celcius)
print(fahrenheit)

print("\n\n\n")
results=[x if x%2 == 0 else 'ODD' for x in range(0,10)]
print(results)

print("\n\n\n")
for x in [1,2,3]:
    for y in [4,5,6]:
        print(x*y)

print("\n\n\n")
print([x*y for x in [1,2,3] for y in [4,5,6]])
