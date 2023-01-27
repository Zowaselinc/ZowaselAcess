"""empty message

Revision ID: 05d0f53eb0dc
Revises: 1d02488f1726
Create Date: 2023-01-20 11:42:45.395797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05d0f53eb0dc'
down_revision = '1d02488f1726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loantransfers', sa.Column('tag', sa.String(length=200), nullable=True))
    op.create_unique_constraint(None, 'loantransfers', ['tag'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'loantransfers', type_='unique')
    op.drop_column('loantransfers', 'tag')
    # ### end Alembic commands ###
