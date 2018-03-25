"""empty message

Revision ID: 69a2f2c071e7
Revises: 47211a326905
Create Date: 2018-03-25 22:26:45.324357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69a2f2c071e7'
down_revision = '47211a326905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alarm', sa.Column('monday', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarm', 'monday')
    # ### end Alembic commands ###
