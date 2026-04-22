x='hello world'
y=['12','hi',-1,9.999]
z=('99.99','hell')
print(len(x))
print(len(y))
print(len(z))
G={'yak':3,'sparrow':4}
print(len(G))




x=5
y='hey'
print(x*3)
print(y*10000)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a=Animal()
a.speak()

d=Dog()
d.speak()
