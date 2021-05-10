#!/usr/bin/env python

metro_areas = [
    ("Tokyo","JP",36.933,(35.689722,139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

for area in metro_areas:
    city, country, population, (longitude, lattitude) = area
    print("city", city)
    print("country", country)
    print("population", population)
    print("longitude", longitude)
    print("lattitude", lattitude)
    print("")

from collections import namedtuple

City = namedtuple("City", "name country population coordinates")

cities = [City(*attrs) for attrs in metro_areas]
print(cities)
