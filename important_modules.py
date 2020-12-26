from collections import Counter
my_list=[1,1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5]
print(Counter(my_list))
my_list2=['a','b','a','b','b']
print(Counter(my_list2))
print(Counter('aaaabbbbaaaaccc'))
sentence="How many time how are you where are you you"
print(Counter(sentence.split()))
c=Counter(sentence.split())
print(Counter(sentence.split()).most_common())
print(c.most_common())


import os

print(os.getcwd())
print(os.listdir('c:\\'))

import shutil
#shutil.move('temp.py','c:\\temp')

print(os.listdir('c:\\temp'))
#os.unlink("c:\\temp\\temp.py")

print(list(range(10)))
