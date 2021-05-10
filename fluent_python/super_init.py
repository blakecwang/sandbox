#!/usr/bin/env python

# https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

class MyParent():
    def __init__(self, my_num):
        self.my_num = my_num

    def __repr__(self):
        return f"my_num: {self.my_num}"

class MyChild(MyParent):
    def __init__(self, my_num):
        super().__init__(my_num)
        self.my_num = self.my_num + 1

child = MyChild(5)
print(child)
