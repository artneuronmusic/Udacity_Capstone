"""empty message

Revision ID: 1306e5201255
Revises: 
Create Date: 2022-06-06 21:16:17.041925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1306e5201255'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('castinglist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movielist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('casting_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['casting_id'], ['castinglist.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movielist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collections')
    op.drop_table('movielist')
    op.drop_table('castinglist')
    # ### end Alembic commands ###
