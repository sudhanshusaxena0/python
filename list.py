#Sort a list
a=[3,1,2,4,2,3,6,2]
a.sort()
print(a)
print(type(a))

#Reverse a list
b=['l','m','a','b','c']
b.reverse()
print(b)

#Append to list
b.append('o')
print(b)
print('Length of b: ',len(b))

b.extend(b[0:5])
print(b)
print('Length of b: ',len(b))

#Sort a list with second element of tuple
c=[('abc',8),('l',6),('lmn',10)]
c.sort(key=lambda x: x[1])
print(c)
print(type(c[0]))

#Pop item from end of list and remove it from list
d=c.pop()
print(d)
print(c)

#Pop first element from list
d=c.pop(0)
print(d)
print(c)

list1=[1]*10
print(list1)
