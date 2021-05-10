#!/usr/bin/env python

import arrow
import yaml
from sqlalchemy import and_, or_

from crud import Session, create_database, drop_database, recreate_database
from model import Case, Member, CaseDetermination

recreate_database()
s = Session()

member = Member(
    client_id="abc",
    external_member_id="123",
    person_code="01"
)
s.add(member)

s.commit()

case0 = Case(
    case_number=1000000000,
    rn="rn0",
    drug_ndc="drug_ndc0",
    origin="fax",
    member_id=member.id,
    prescriber_npi="0123456789",
    requester_type="pharmacy",
)
s.add(case0)

case1 = Case(
    case_number=1000000001,
    rn="rn1",
    drug_ndc="drug_ndc1",
    origin="epa",
    member_id=member.id,
    prescriber_npi="0123456789",
    requester_type="prescriber",

    original_case_number=1000000000,
    original_case_relationship="reconsideration",
)
s.add(case1)

s.commit()

determination = CaseDetermination(
    case_number=case0.case_number,
    created_at=arrow.now(),
    result="approved",
    reason="it was dope",
    determiner_email="patech@cap-rx.com",
)
s.add(determination)

s.commit()

#members = s.query(Member).all()
#cases = s.query(Case).all()
#determinations = s.query(CaseDetermination).all()

res = (
    s.query(Member.id, Case.case_number, CaseDetermination.result)
    .outerjoin(Case, Member.id == Case.member_id)
    .outerjoin(CaseDetermination, Case.case_number == CaseDetermination.case_number)
).all()

for item in res:
    print(item)
    print("")

#breakpoint()

#print("cases", cases)
#print("member", member)
#print("determination", determination)
#stuff = cases + members + determinations
#for thing in stuff:
#    print(thing.__class__)
#    print(thing.__dict__)
#    print("")

s.close()
