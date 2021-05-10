#!/usr/bin/env python

#from sqlalchemy.sql.schema import FetchedValue
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
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
    __table_args__ = (
        CheckConstraint(
            (
                "(original_case_number is not null and "
                "original_case_relationship is not null) or "
                "(original_case_number is null and "
                "original_case_relationship is null)"
            ),
            "case_original_case_relationship_null_check",
        ),
        UniqueConstraint("rn", name="rn_uniq"),
    )


    # basic case info

    case_number = Column(
        BigInteger,
        # ensures 10-digit number without having to use Text
        CheckConstraint(
            "case_number >= 1000000000 and case_number < 10000000000",
            "case_number_range_check",
        ),
        primary_key=True,
    )

    case_type = Column(
        Text,
        CheckConstraint(
            "case_type in ('pre_service', 'concurrent', 'post_service')",
            "case_type_check",
        ),
    )

    rn = Column(
        Text,
        nullable=False,
#        server_default=FetchedValue(),
#        server_onupdate=FetchedValue(),
    )

    origin = Column(
        Text,
        CheckConstraint(
            "origin in ('fax', 'phone', 'epa')",
            "case_origin_check",
        ),
        nullable=False,
    )

    urgent = Column(
        Boolean,
        nullable=False,
        default=False,
    )


    # case-to-case relationships

    original_case_number = Column(
        BigInteger,
        ForeignKey(
            "cases.case_number",
            ondelete="cascade",
            onupdate="cascade",
        ),
    )

    original_case = relationship(
        "Case",
        backref="related_cases",
        remote_side=case_number,
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
                    "'peer_to_peer',"
                    "'duplicate'"
                ")"
            ),
            "case_original_case_relationship_check",
        ),
    )


    # drug info

    drug_ndc = Column(
        Text,
        nullable=False,
    )


    # member, prescriber, requester info

    member = Column(
        # {"client_id":"123","external_member_id":"abc","person_code":"01"}
        postgresql.JSON,
        nullable=False,
    )

    prescriber_npi = Column(
        Text,
        CheckConstraint(
            "prescriber_npi ~ '^[0-9]{10}$'",
            "case_prescriber_npi_check",
        ),
        nullable=False,
    )

    requester_type = Column(
        Text,
        CheckConstraint(
            "requester_type in ('member', 'pharmacy', 'prescriber')",
            "case_requester_type_check",
        ),
        nullable=False,
    )
