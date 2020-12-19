#Sort a list
a=[3,1,2,4,2,3,6,2]
a.sort()
print(a)
#Sort a list with second element of tuple
a=[('abc',8),('l',6),('lmn',10)]
a.sort(key=lambda x: x[1])
print(a)
