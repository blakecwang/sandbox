#!/usr/bin/env python

#from sqlalchemy.sql.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func
from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Column,
    ForeignKey,
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
)
from sqlalchemy_utils import ArrowType

from crud import Base


class Member(Base):

    __tablename__ = "members"
    __table_args__ = (
        UniqueConstraint(
            "client_id",
            "external_member_id",
            "person_code",
            name="members_client_external_person_code_uniq",
        ),
    )

    id = Column(BigInteger, primary_key=True)

    client_id = Column(Text, nullable=False)

    external_member_id = Column(Text, nullable=False)

    person_code = Column(Text, nullable=False)

    cases = relationship("Case", backref="member")


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
        unique=True,
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

    urgent = Column(Boolean, nullable=False, default=False)

    # case-to-case relationships

    original_case_number = Column(
        BigInteger,
        ForeignKey("cases.case_number", ondelete="cascade", onupdate="cascade"),
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

    drug_ndc = Column(Text, nullable=False)

    # member, prescriber, requester info

    member_id = Column(
        BigInteger,
        ForeignKey("members.id", ondelete="cascade", onupdate="cascade"),
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


class CaseDetermination(Base):

    __tablename__ = "case_determinations"
    __table_args__ = (
        PrimaryKeyConstraint(
            "case_number",
            "created_at",
            "determiner_email",
            "result",
            "reason",
        ),
    )

    case_number = Column(
        BigInteger,
        ForeignKey("cases.case_number", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )

    created_at = Column(
        ArrowType(timezone=True),
        server_default=func.clock_timestamp(),
        nullable=False,
    )

    determiner_email = Column(Text, nullable=False)

    result = Column(
        Text,
        CheckConstraint(
            "result in ('approved', 'denied', 'closed')",
            "case_determination_result_check",
        ),
        nullable=False,
    )

    reason = Column(Text, nullable=False)
