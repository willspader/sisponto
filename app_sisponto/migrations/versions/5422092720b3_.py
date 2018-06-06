"""empty message

Revision ID: 5422092720b3
Revises: bdd1c4f55cb0
Create Date: 2018-06-05 02:09:44.638229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5422092720b3'
down_revision = 'bdd1c4f55cb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBRelUsuProj', schema=None) as batch_op:
        batch_op.drop_column('user_id')
        batch_op.drop_column('projeto')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBRelUsuProj', schema=None) as batch_op:
        batch_op.add_column(sa.Column('projeto', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
