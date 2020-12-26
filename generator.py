def create_cubes(n):
    for x in range(n):
        yield x**3 #Yield is memory efficient

for i in create_cubes(10):
    print(i)

print(list(create_cubes(10)))

#Not memory efficient
def gen_fibon(n):
    a=1
    b=1
    output=[]

    for i in range(n):
        output.append(a)
        a,b=b,a+b
    return output

for number in gen_fibon(10):
    print(number)

#memory efficient
def gen_fibon1(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x

g=simple_gen()
print(next(g))
print(next(g))
print(next(g))

print()

s="sudhanshu"
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print()

my_list=[1,2,3,4,5,6,7,8]
gencomp=(item for item in my_list if item > 3)
for item in gencomp:
    print(item)
