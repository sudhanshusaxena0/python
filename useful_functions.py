#map function
def ascii_value(x):
    return ord(x)

a=['a','b','c']
for item in map(ascii_value,a):
    print(item)

print(list(map(ascii_value,a)))

#filter function is same as map but it removes None values from output
def check_even(num):
    if num%2 == 0:
        return num

a=[1,2,3,4,5,6,7,8,9,10]
print(list(map(check_even,a)))
print(list(filter(check_even,a)))

#lambda expresstion
def square(num):
    return num**2
print(square(5))

num=3
square1=lambda num: num**2
print(square1(6))

a=[1,2,3,4,5,6,7,8,9,10]
b=list(map(lambda n:n**2,a))
print(b)

b=list(map(lambda n:n%2 == 0,a))
print(b)

b=list(filter(lambda n:n%2 == 0,a))
print(b)

names=["ayush","piyush","ram"]
print(list(map(lambda name:name[0],names)))
print(list(map(lambda name:name[::-1],names)))

def sequence_check(list1):
    list2=[0,0,7]
    index1=0
    list3=[]
    for i in list1:
        if i == list2[index1]:
            list3[index1]=i
            index1+=1
            if list2 == list3:
                return True
        else
            index1=0
