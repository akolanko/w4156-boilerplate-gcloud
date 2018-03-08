"""empty message

Revision ID: f3a4549c1fbe
Revises: 29ee7f7b6226
Create Date: 2018-03-07 21:18:38.624791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3a4549c1fbe'
down_revision = '29ee7f7b6226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=4), autoincrement=False, nullable=True),
    sa.Column('email', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=64), nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
