"""all tables

Revision ID: 4b795622ce25
Revises: 
Create Date: 2020-03-31 22:22:30.959006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b795622ce25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_owner_name'), 'owner', ['name'], unique=False)
    op.create_table('puppy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('tag', sa.String(length=100), nullable=False),
    sa.Column('photos', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_puppy_name'), 'puppy', ['name'], unique=False)
    op.create_index(op.f('ix_puppy_tag'), 'puppy', ['tag'], unique=False)
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    op.drop_index(op.f('ix_puppy_tag'), table_name='puppy')
    op.drop_index(op.f('ix_puppy_name'), table_name='puppy')
    op.drop_table('puppy')
    op.drop_index(op.f('ix_owner_name'), table_name='owner')
    op.drop_table('owner')
    # ### end Alembic commands ###