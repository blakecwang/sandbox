#!/usr/bin/env python

from crud import Session
from models import Bass

s = Session()

for bass in s.query(Bass).all():
    price = input(f"Price for '{bass.num_strings}-string {'fretted' if bass.has_frets else 'fretless'} {bass.make}': $")
    bass.price = price
    # .add() takes care of UPDATEs too!
    s.add(bass)

s.commit()
s.close()
