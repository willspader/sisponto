"""empty message

Revision ID: 08c2c13b26e1
Revises: a7ce834a8f6d
Create Date: 2018-06-17 13:48:49.648116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08c2c13b26e1'
down_revision = 'a7ce834a8f6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBProjeto', schema=None) as batch_op:
        batch_op.alter_column('descricaoProj',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TBProjeto', schema=None) as batch_op:
        batch_op.alter_column('descricaoProj',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)

    # ### end Alembic commands ###
