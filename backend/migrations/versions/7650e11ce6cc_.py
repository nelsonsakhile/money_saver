"""empty message

Revision ID: 7650e11ce6cc
Revises: fb43a3f328fd
Create Date: 2024-12-03 15:45:16.670691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7650e11ce6cc'
down_revision = 'fb43a3f328fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_depature', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('date_return', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.drop_column('date_return')
        batch_op.drop_column('date_depature')

    # ### end Alembic commands ###
