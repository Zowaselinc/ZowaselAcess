"""empty message

Revision ID: 246b63cf905b
Revises: 426d7f16f721
Create Date: 2023-02-01 09:18:23.946423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246b63cf905b'
down_revision = '426d7f16f721'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'crop_card', ['mobile'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'crop_card', type_='unique')
    # ### end Alembic commands ###
