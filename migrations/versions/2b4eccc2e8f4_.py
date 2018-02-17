"""empty message

Revision ID: 2b4eccc2e8f4
Revises: c0b37445be15
Create Date: 2018-02-17 21:35:21.409094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b4eccc2e8f4'
down_revision = 'c0b37445be15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    # ### end Alembic commands ###
