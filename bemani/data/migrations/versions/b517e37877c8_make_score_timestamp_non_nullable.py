"""Make score timestamp non-nullable.

Revision ID: b517e37877c8
Revises: 3f621cef0a71
Create Date: 2017-03-21 20:36:11.425736

"""
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b517e37877c8'
down_revision = '3f621cef0a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('score', 'timestamp',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('score', 'timestamp',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###