"""empty message

Revision ID: bdd1c4f55cb0
Revises: 81acfa0a00df
Create Date: 2018-06-03 15:59:07.365548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd1c4f55cb0'
down_revision = '81acfa0a00df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TBRelUsuProj',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_projeto', sa.Integer(), nullable=True),
    sa.Column('is_coordenador', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_projeto'], ['TBProjeto.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TBRelUsuProj')
    # ### end Alembic commands ###
