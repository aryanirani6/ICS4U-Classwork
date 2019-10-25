"""class Person:
    pass


p = Person()
p.name = "Jeff"

p.eye_colour = "Blue"

print(p)
print(p.name)

print(p.eye_colour)
"""

# Init method

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

p = Person("Jeff", 34)
p2 = Person("Sally", 55)
print(p.name, p.age)
print(p2.name, p2.age)
"""
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    Person("a", 1),
    Person("b", 2),
    Person("c", 3),
    Person("d", 4),
    Person("e", 5)
]
 
for person in people:
    print(person.name)
"""

"""a = 5
b = a # copies over the value
print(a) #5
print(b) #5


a = 10

print(a) # 10
print(b) # 5
"""

class Person:
    pass

a = Person()
b = a
print(a)
print(b)
b.name = "Jeff"
print(a.name)

del b

print(a)
print(b)
