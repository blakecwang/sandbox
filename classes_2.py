#!/usr/bin/env python

class Automobile:
    class_var = "class_var_val"

    def __init__(self, kind, make, model):
        self.kind = kind
        self.make = make
        self.model = model

    def output(self):
        return f"[{self.class_var}]You drive a {self.make} {self.model}, which is a {self.kind}"

my_car = Automobile("mid-sized SUV", "Audi", "Q7")
print("kind", my_car.kind)
print("make", my_car.make)
print("model", my_car.model)
print(my_car.output())
