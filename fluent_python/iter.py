#!/usr/bin/env python

vowels = "a e i o u".split()
vowels_iter = iter(vowels)

print("vowels iterator")
print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'


class PrintNumber():
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 0

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max_num:
            raise StopIteration

        self.num += 1
        return self.num

print("custom class with special methods __iter__() and __next__() implemented")
printer = PrintNumber(3)
printer_iter = iter(printer)
print(next(printer_iter))
print(next(printer_iter))


class DoubleIt():
    def __init__(self):
        self.val = 1

#    def __iter__(self):
#        return self

    def __next__(self):
        self.val *= 2
        return self.val

    __call__ = __next__

print("iter using sentinel")
double_iter = iter(DoubleIt(), 64)
for val in double_iter:
    print(val)
