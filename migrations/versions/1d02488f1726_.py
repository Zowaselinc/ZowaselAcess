"""empty message

Revision ID: 1d02488f1726
Revises: ddb58a074109
Create Date: 2023-01-07 10:32:23.926320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1d02488f1726'
down_revision = 'ddb58a074109'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score_card', 'term_months')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score_card', sa.Column('term_months', mysql.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###
