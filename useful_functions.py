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


def check_palindrome(str1):
    str1=str1.replace(" ","")
    if str1 == str1[::-1]:
        print(f"String {str1} is a palindrome")
    else:
        print(f"String {str1} is not a palindrome")

check_palindrome("nurses run")
check_palindrome("abc xyz")
