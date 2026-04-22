# #num = 20
# #print(type(num))

# #num2 = 20.5
# #print(type(num2))

# name = "Python"
# print(type(name))

# name1 = {"name": "Python"}
# print(type(name1))

# num3 = {1,2,3,4,5}
# print(type(num3))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def __repr__(self):
        return f"Person(name='{self.name!r}', age={self.age!r})"


p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1)            #person(name='Alice', age=25)        
print(p1.greet())    #Hi, I'm Alice and I'm 25 years old.
print(p2)            #person(name='Bob', age=30)
print(p2.name, p2.age) 