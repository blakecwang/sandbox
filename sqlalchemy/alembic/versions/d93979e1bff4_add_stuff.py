"""Add stuff

Revision ID: d93979e1bff4
Revises: 
Create Date: 2021-05-10 22:25:03.196439

"""
from alembic import op
from sqlalchemy_utils import ArrowType
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93979e1bff4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('client_id', sa.Text(), nullable=False),
    sa.Column('external_member_id', sa.Text(), nullable=False),
    sa.Column('person_code', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('client_id', 'external_member_id', 'person_code', name='members_client_external_person_code_uniq')
    )
    op.create_table('cases',
    sa.Column('case_number', sa.BigInteger(), nullable=False),
    sa.Column('case_type', sa.Text(), nullable=True),
    sa.Column('rn', sa.Text(), nullable=False),
    sa.Column('origin', sa.Text(), nullable=False),
    sa.Column('urgent', sa.Boolean(), nullable=False),
    sa.Column('original_case_number', sa.BigInteger(), nullable=True),
    sa.Column('original_case_relationship', sa.Text(), nullable=True),
    sa.Column('drug_ndc', sa.Text(), nullable=False),
    sa.Column('member_id', sa.BigInteger(), nullable=False),
    sa.Column('prescriber_npi', sa.Text(), nullable=False),
    sa.Column('requester_type', sa.Text(), nullable=False),
    sa.CheckConstraint('(original_case_number is not null and original_case_relationship is not null) or (original_case_number is null and original_case_relationship is null)', name='case_original_case_relationship_null_check'),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['original_case_number'], ['cases.case_number'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('case_number'),
    sa.UniqueConstraint('rn')
    )
    op.create_table('case_determinations',
    sa.Column('case_number', sa.BigInteger(), nullable=False),
    sa.Column('created_at', ArrowType(timezone=True), server_default=sa.text('clock_timestamp()'), nullable=False),
    sa.Column('determiner_email', sa.Text(), nullable=False),
    sa.Column('result', sa.Text(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['case_number'], ['cases.case_number'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('case_number', 'created_at', 'determiner_email', 'result', 'reason')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('case_determinations')
    op.drop_table('cases')
    op.drop_table('members')
    # ### end Alembic commands ###
