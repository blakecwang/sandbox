#!/usr/bin/env python

import arrow
import yaml
from sqlalchemy import and_, or_

from crud import Session, create_database, drop_database, recreate_database
from model import Case

recreate_database()
s = Session()

case = Case(
    case_number=1000000000,
    rn="rn",
    created_by="not json",
#    created_by={"email":"person@cap-rx.com"}
)

s.add(case)

s.commit()

cases = s.query(Case).all()
breakpoint()
print(cases)

s.close()
