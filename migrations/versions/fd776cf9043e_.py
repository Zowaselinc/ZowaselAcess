"""empty message

Revision ID: fd776cf9043e
Revises: 05d0f53eb0dc
Create Date: 2023-01-28 09:48:04.511362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fd776cf9043e'
down_revision = '05d0f53eb0dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.alter_column('loans', 'type',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('loans', 'company',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('loans', 'repayment_months',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('loans', 'interest_rate_per_annum',
               existing_type=mysql.INTEGER(),
               nullable=False)
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.alter_column('loans', 'interest_rate_per_annum',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('loans', 'repayment_months',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('loans', 'company',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('loans', 'type',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    
    # ### end Alembic commands ###