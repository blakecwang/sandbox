#!/usr/bin/env python

from math import hypot

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, to_add):
        if not isinstance(to_add, Vector):
            raise Exception

        return Vector(self.x + to_add.x, self.y + to_add.y)

    def __mul__(self, scalar):
        if not (isinstance(scalar, int) or isinstance(scalar, float)):
            raise Exception

        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x},{self.y})"

    def __bool__(self):
        return bool(self.x or self.y)

v1 = Vector(3, 4)
print("magnitude")
print(abs(v1))
v2 = Vector(4, 3)
v3 = v1 + v2
print("vector addition")
print(v3)
print(abs(v3))
print("scalar multiplication")
v4 = v1 * 100
print(v4)
print(abs(v4))
