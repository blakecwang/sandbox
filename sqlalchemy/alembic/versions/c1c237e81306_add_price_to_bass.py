"""Add price to Bass

Revision ID: c1c237e81306
Revises: 
Create Date: 2021-04-22 23:22:34.291193

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c1c237e81306'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('basses', sa.Column('price', postgresql.MONEY(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('basses', 'price')
    # ### end Alembic commands ###
