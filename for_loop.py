list=[2,1,3,4,2,3,54,6,75,5434]
for i in list:
    print(f"Hello {i}")

dict={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

for key,value in dict.items():
    print(f"Key is {key} and value is {value}")

for num in list:
    if num % 2 == 0:
        print(f"Even: {num}")
    else:
        print(f"Odd: {num}")

list_sum=0
print(list)
for i in list:
    list_sum=list_sum + i
    print(list_sum)

name="Sudhanshu Sinha"
for i in name:
    print(i)

for i in "Sudhanshu Sinha":
    print(i)

for _ in list:
    print("list")

t=[(1,2),(3,4),(5,6)]
for items in t:
    print(items)

for (a,b) in t:
    print(f"first: {a} second: {b}")

for a,b in t:
    print(f"first: {a} second: {b}")

t1=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for a,b,c in t1:
    print(f"a is {a}, b is {b}, c is {c}")

dict={'key1':'value1','key2':'value2','key3':'value3'}
for key,value in dict.items():
    print(f"key is {key} and value is {value}")

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)
