class Cat():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says meow"

class Dog():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says wow"

niko=Dog("niko")
felix=Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        raise NotImpletementedError("Subclass must implement thais abstract method")

class Dog(Animal):
    def speak(self):
        return self.name+" says woof!"

class Cat(Animal):
    def speak(self):
        return self.name+" says meow!"

fido=Dog("Fido")
iris=Cat("Iris")


print(fido.speak())
print(iris.speak())
#print(Animal.speak("check error"))


class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b=Book("abc","xyz",20)
print(b)
print(len(b))

#Delete a variable from memory
del b
print(b)
