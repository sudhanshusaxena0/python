def sample_function():
    print("This is a sample function")

sample_function()

def sample_function2(name):
    print(f"This is a {name}")
    return "sample_function2 executed successfully."

result=sample_function2("sample_function2")
print(result)

def add_function(num1,num2):
    return num1+num2

print(add_function(100,200))

#Set some default values for parameters
def add_function2(num1=500,num2=1000):
    return num1+num2

print(add_function2())
print(add_function2(5000,10000))

def check_even(num):
    return num%2 == 0

print(check_even(10))
print(check_even(11))

def check_even2(num_list):
    for i in num_list:
        if i%2 == 0:
            return True
        else:
            pass
    return False

print(check_even2([1,4,5,6]))
print(check_even2([1,2,3]))
print(check_even2([1,3,5]))

def check_even3(num_list):
    even_list=[]

    for i in num_list:
        if i%2 == 0:
            even_list.append(i)
        else:
            pass
    return even_list

print(check_even3([1,2,3,4,5,6,7,8,9,10]))

prices=[('mango',10),('orange',8),('banana',6),('pineapple',40)]

for i in prices:
    print(i)

for fruit,price in prices:
    print(fruit)
    print(price)

def check_costly_fruit(fruits):
    fruit_max=''
    cost_max=0
    for fruit,cost in fruits:
        if cost > cost_max:
            cost_max=cost
            fruit_max=fruit
        else:
            pass
    return (fruit_max,cost_max)

print(check_costly_fruit(prices))
fruit,cost=check_costly_fruit(prices)
print(f"{fruit} cost is {cost}")

example=[1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)

my_list=['0',' ',' ']
print(my_list)

def shuffle_mylist(mylist):
    shuffle(mylist)
    return mylist
print(shuffle_mylist(my_list))

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0,1, or 2: ")
    return int(guess)

player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

check_guess(my_list,player_guess())

#arbiterary number of parameters with * and saves the parameters as tuple
def add_num(*nums):
    print(nums)
    return sum(nums)

print(add_num(1,2,3,4))

#arbitrary number of key vale pairs with ** and save the parameters as dictionary
def myfunc(**dict1):
    print(dict1)
    if 'fruit' in dict1:
        print(f"My fruit of choice is {dict1['fruit']}")

myfunc(fruit="apple",veggie="beans")

def myfunc1(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")
myfunc1(10,20,30,fruit="orange",food="eggs",animal="dog")

#return string with even index character in upper and odd index character in lower
def upper_lower(string1):
    case_string=""
    for i in range(len(string1)):
        if i%2 == 0:
            case_string=case_string+string1[i].upper()
        else:
            case_string=case_string+string1[i].lower()

    return case_string

result=upper_lower("sudhanshu")
print(result)

#return string with even ascii character in upper and odd ascii character in lower
def upper_lower1(string1):
    case_string=""
    for i in string1:
        if ord(i)%2 == 0:
            case_string=case_string+i.upper()
        else:
            case_string=case_string+i.lower()

    return case_string

result=upper_lower1("sudhanshu")
print(result)

def max_min(num1,num2):
    if num1%2 == 0 and num2%2 == 0:
        return max(num1,num2)
    else:
        return min(num1,num2)

print(max_min(2,4))
print(max_min(3,5))

#convert a list into string
list1=["sudhanshu","sinha","age","is","38"]
print(" ".join(list1))

#absolute value
print(abs(-100))

#for i in range(3):
#    for j in range(3,0):
def triangleShape(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()

triangleShape(5)



def triangle(num):
    for i in range(num):
        for j in range(num-i):
            print("   ",end=" ")
        for k in range(i*2+1):
            print(" * ",end=" ")
        print()

triangle(5)

def tree(num):
    x=num
    y=num-1
    z=0
    while z < num:
        print(" "*z,end="")
        print("*"*(x+y),end="")
        z+=1
        x-=1
        y-=1
        print()
    x=num-2
    y=num-1
    z=0
    while z < num-1:
        print(" "*x,end="")
        print("*"*y,end="")
        x-=1
        y+=2
        z+=1
        print()
