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

info=help(c)
print(info)
