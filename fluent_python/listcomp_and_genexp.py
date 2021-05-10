#!/usr/bin/env python

sizes = "S M L".split()
colors = "Black White Red Blue".split()
sexes = "Men Women".split()

print(
    "listcomp",
    [(sex, color, size) for size in sizes
                        for color in colors
                        for sex in sexes],
)

print(
    "genexp with tuple",
    tuple((color, size) for size in sizes for color in colors),
)

symbols = '$¢£¥€¤'
print(
    "another genexp with tuple",
    tuple(ord(symbol) for symbol in symbols),
)

import array

print(
    "genexp with array.array",
    array.array('I', (ord(symbol) for symbol in symbols)),
)
