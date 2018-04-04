"""add alarm active indicator

Revision ID: 2a6180fc6d75
Revises: 61e2df193173
Create Date: 2018-04-03 10:54:28.158250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a6180fc6d75'
down_revision = '61e2df193173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alarm', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarm', 'active')
    # ### end Alembic commands ###