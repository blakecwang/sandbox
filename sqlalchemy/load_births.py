#!/usr/bin/env python

import numpy as np
from sqlalchemy import Column, CheckConstraint, BigInteger, Integer

from crud import Session

def load_data(filename):
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        converters={0: lambda s: str(s)},
        usecols=np.arange(0,7),
    )
    return data.tolist()

filename = "/home/sandbox/vmshare/births.csv"
data = load_data(filename)
breakpoint()

##recreate_database()
#s = Session()
#
#try:
#    filename = "/home/sandbox/vmshare/births.csv"
#    data = load_data(filename)
#    breakpoint()
#
#    for i in data:
#        breakpoint()
#        record = Birth(
#            year=i[0],
#            district_code=i[1],
#            district_name=i[2],
#            neighborhood_code=i[3],
#            neighborhood_name=i[4],
#            gender=i[5],
#            number=i[6],
#        )
#        breakpoint()
#        exit()
#        s.add(record)
#
#    s.commit()
#    print("IT WORKED!")
#except Exception as err:
#    print(err)
#    s.rollback()
#finally:
#    s.close()
