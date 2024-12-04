"""empty message

Revision ID: 4c54f4944c94
Revises: 7650e11ce6cc
Create Date: 2024-12-03 16:03:18.744014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c54f4944c94'
down_revision = '7650e11ce6cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.alter_column('date_depature',
               existing_type=sa.DATETIME(),
               type_=sa.TIMESTAMP(),
               existing_nullable=True)
        batch_op.alter_column('date_return',
               existing_type=sa.DATETIME(),
               type_=sa.TIMESTAMP(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.alter_column('date_return',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('date_depature',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
