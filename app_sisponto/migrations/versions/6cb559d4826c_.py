"""empty message

Revision ID: 6cb559d4826c
Revises: 4472dac3ce0d
Create Date: 2018-06-05 22:26:36.238689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cb559d4826c'
down_revision = '4472dac3ce0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBRelUsuProj', schema=None) as batch_op:
        batch_op.drop_column('user_id')
        batch_op.drop_column('projeto_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBRelUsuProj', schema=None) as batch_op:
        batch_op.add_column(sa.Column('projeto_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###