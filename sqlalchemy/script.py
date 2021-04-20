#!/usr/bin/env python

import arrow
import yaml
from sqlalchemy import and_, or_

from crud import Session, create_database, drop_database, recreate_database
from models import Bass

recreate_database()

s = Session()

now = arrow.now()
start_time = now.shift(hours=-5)
end_time = now.shift(hours=5)

# yuck, hacky
i = 0
for all_data in yaml.load_all(open("basses.yaml"),  Loader=yaml.FullLoader):
    for _key, data in all_data.items():
        data["created_at"] = now.shift(hours=-i)
        bass = Bass(**data)
        s.add(bass)
        i += 1

s.commit()

#res = s.query(Bass).first()
#res = s.query(Bass).all()
#res = s.query(Bass).filter_by(make="Fender").all()
#res = s.query(Bass).filter(Bass.num_strings == 4).all()
#res = s.query(Bass).filter(Bass.make.ilike("gibson")).first()
#res = s.query(Bass).filter(Bass.created_at.between(start_time, end_time)).count()
#res = s.query(Bass).filter(
#    and_(
#        Bass.created_at.between(start_time, end_time),
#        Bass.make.ilike("gibson")
#    )
#).all()
#res = s.query(Bass).filter(
#    or_(
#        Bass.make.ilike("fender"),
#        Bass.make.ilike("gibson")
#    )
#).all()
#res = s.query(Bass).order_by(Bass.created_at.desc()).first()
#res = s.query(Bass).limit(2).all()
res = s.query(Bass).filter(
    and_(
        or_(
            Bass.make.ilike("fender"),
            Bass.make.ilike("IBANEZ"),
        ),
        Bass.created_at.between(start_time, end_time),
    ),
)\
.order_by(Bass.created_at.asc())\
.limit(2)\
.first()

print(res)

s.close()
