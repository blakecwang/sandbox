#!/usr/bin/env python

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

YEAR = slice(0, 6)
DESC = slice(6, 40)
AMNT = slice(40, 52)
QNTY = slice(52, 55)
TOTL = slice(55, None)

lines = invoice.split("\n")[2:-1]
for line in lines:
    print("YEAR", line[YEAR].strip())
    print("DESC", line[DESC].strip())
    print("AMNT", line[AMNT].strip())
    print("QNTY", line[QNTY].strip())
    print("TOTL", line[TOTL].strip())
    print("")
