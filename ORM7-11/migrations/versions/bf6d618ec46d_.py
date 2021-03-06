"""empty message

Revision ID: bf6d618ec46d
Revises: 1dff26d0a6ec
Create Date: 2021-09-23 14:30:27.004045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf6d618ec46d'
down_revision = '1dff26d0a6ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('idade', sa.String(), nullable=False),
    sa.Column('genero', sa.String(), nullable=False),
    sa.Column('cachorro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cachorro_id'], ['cachorros.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cachorro_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donos')
    # ### end Alembic commands ###
