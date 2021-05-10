#!/usr/bin/env python

import arrow
import yaml
from sqlalchemy import and_, or_

from crud import Session, create_database, drop_database, recreate_database
from model import Case

recreate_database()
s = Session()

case0 = Case(
    case_number=1000000000,
    rn="rn0",
    drug_ndc="drug_ndc0",
    created_by={"email":"person@cap-rx.com"}
)
s.add(case0)

case1 = Case(
    case_number=1000000001,
    original_case_number=1000000000,
    original_case_relationship="reconsideration",
    rn="rn1",
    drug_ndc="drug_ndc1",
    created_by={"email":"person@cap-rx.com"}
)
s.add(case1)

s.commit()

cases = s.query(Case).all()

#breakpoint()

print(cases)

s.close()
