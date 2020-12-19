import time
x=0
while x<10:
    print(f'Current value of x is {x}')
    x=x+1
while x<10:
    print(f'Current value of x is {x}')
    x+=1
else:
    print(f'x {x} is not less than 10')

x=10
while x>=0:
    print(x)
    x-=1

time.sleep(10)
print("\n\n\n")

#pass is just to keep running loop without action to avoid any error if no statement inside loop
x=[1,2,3,4,5,6]
for item in x:
    pass
print(item)
print("\n\n\n")

x=[1,2,3,4,5,6]
for item in x:
    if item == 3:
        continue
    print(item)
print("\n\n\n")

x=[1,2,3,4,5,6]
for item in x:
    if item == 3:
        break
    print(item)
