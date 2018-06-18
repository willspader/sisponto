"""empty message

Revision ID: 22dd1484ce37
Revises: 08c2c13b26e1
Create Date: 2018-06-17 21:09:04.571186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22dd1484ce37'
down_revision = '08c2c13b26e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TBRegistroDias')
    op.drop_table('TBAtividades')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TBAtividades',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('descricaoAtiv', sa.VARCHAR(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TBRegistroDias',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('datahr_inicio', sa.VARCHAR(length=19), nullable=True),
    sa.Column('datahr_fim', sa.VARCHAR(length=19), nullable=True),
    sa.Column('descricao', sa.VARCHAR(length=256), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('projeto_id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
