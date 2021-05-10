#!/usr/bin/env python

#from sqlalchemy.sql.schema import FetchedValue
from sqlalchemy.dialects import postgresql
from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Column,
    DDL,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Text,
    UniqueConstraint,
)

from crud import Base

"""
Case version is determined by 'original_case_relationship'. If that field is
empty, then it's a new case.

This implementation does NOT handle:
    - cases for anything but a single drug
"""

class Case(Base):

    __tablename__ = "cases"

    case_number = Column(
        BigInteger,
        CheckConstraint(
            "case_number >= 1000000000 and case_number < 10000000000",
            "case_number_range_check",
        ),
        primary_key=True
    )

    rn = Column(
        Text,
        nullable=False,
#        server_default=FetchedValue(),
#        server_onupdate=FetchedValue(),
    )

    created_by = Column(
        postgresql.JSON,
        nullable=False,
    )

    assignee_email = Column(
        Text,
    )

    drug_ndc = Column(
        Text,
        nullable=False,
    )

    original_case_number = Column(
        BigInteger,
        ForeignKey(
            "cases.case_number",
            ondelete="cascade",
            onupdate="cascade",
        ),
    )

    original_case_relationship = Column(
        Text,
        CheckConstraint(
            (
                "original_case_relationship in ("
                    "'reconsideration',"
                    "'appeal_1',"
                    "'appeal_2',"
                    "'appeal_3',"
                    "'peer-to-peer',"
                    "'duplicate'"
                ")"
            ),
            "case_original_case_relationship_check"
        )
    )

    __table_args__ = (
        CheckConstraint(
            (
                "(original_case_number is not null and "
                "original_case_relationship is not null) or "
                "(original_case_number is null and "
                "original_case_relationship is null)"
            )
        ),
    )
