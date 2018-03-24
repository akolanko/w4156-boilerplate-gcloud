"""empty message

Revision ID: 0400ec0a51ad
Revises: 2a948fe5e468
Create Date: 2018-03-24 14:44:37.520356

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0400ec0a51ad'
down_revision = '2a948fe5e468'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'work')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('work', mysql.VARCHAR(length=32), nullable=True))
    # ### end Alembic commands ###
