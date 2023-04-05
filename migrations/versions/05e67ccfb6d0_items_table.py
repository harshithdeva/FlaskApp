"""Items table

Revision ID: 05e67ccfb6d0
Revises: f76fdfea612e
Create Date: 2023-04-05 22:04:42.074108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05e67ccfb6d0'
down_revision = 'f76fdfea612e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=255), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###