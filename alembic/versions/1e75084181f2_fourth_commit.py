"""fourth commit

Revision ID: 1e75084181f2
Revises: 999c48b1cb87
Create Date: 2022-03-18 16:43:46.856720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e75084181f2'
down_revision = '999c48b1cb87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_name', sa.String(length=50), nullable=True),
    sa.Column('car_plate', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cars_car_name'), 'cars', ['car_name'], unique=True)
    op.create_index(op.f('ix_cars_car_plate'), 'cars', ['car_plate'], unique=True)
    op.create_index(op.f('ix_cars_id'), 'cars', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cars_id'), table_name='cars')
    op.drop_index(op.f('ix_cars_car_plate'), table_name='cars')
    op.drop_index(op.f('ix_cars_car_name'), table_name='cars')
    op.drop_table('cars')
    # ### end Alembic commands ###
