"""empty message

Revision ID: c0b37445be15
Revises: 97c422938533
Create Date: 2018-02-17 15:51:58.318130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0b37445be15'
down_revision = '97c422938533'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('progresses', sa.Column('removed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('progresses', 'removed')
    # ### end Alembic commands ###
