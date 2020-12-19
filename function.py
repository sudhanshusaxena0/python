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
