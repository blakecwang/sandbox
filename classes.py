#!/usr/bin/env python

class Person:
    class_attr = "this is a class attribute"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old!"


blake = Person("Blake", 31)
print(blake.name)
print(blake.greeting())

# del blake.age
# print(blake.greeting()) => AttributeError: 'Person' object has no attribute 'age'

print(Person.class_attr)

class EmptyClass:
    pass
