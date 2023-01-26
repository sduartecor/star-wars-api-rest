"""empty message

Revision ID: 053a18c30c7d
Revises: 2ea44aaafe57
Create Date: 2023-01-26 13:12:46.956797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '053a18c30c7d'
down_revision = '2ea44aaafe57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('vehicle_class', sa.String(length=250), nullable=False),
    sa.Column('manufacturer', sa.String(length=250), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.Column('max_atmospheric_speed', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    # ### end Alembic commands ###
