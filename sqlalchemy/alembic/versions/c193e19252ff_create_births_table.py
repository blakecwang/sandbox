"""Create births table

Revision ID: c193e19252ff
Revises: c1c237e81306
Create Date: 2021-05-02 18:54:33.162787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c193e19252ff'
down_revision = 'c1c237e81306'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('births',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('year', sa.VARCHAR(length=4), nullable=True),
        sa.Column('district_code', sa.Integer(), nullable=True),
        sa.Column('district_name', sa.VARCHAR(length=255), nullable=True),
        sa.Column('neighborhood_code', sa.Integer(), nullable=True),
        sa.Column('neighborhood_name', sa.VARCHAR(length=255), nullable=True),
        sa.Column('gender', sa.VARCHAR(length=255), nullable=True),
        sa.Column('number', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('births')
    # ### end Alembic commands ###
