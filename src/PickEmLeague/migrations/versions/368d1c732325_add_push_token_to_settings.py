"""add push token to settings

Revision ID: 368d1c732325
Revises: 49b4cc7895ba
Create Date: 2023-10-13 12:05:49.035246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '368d1c732325'
down_revision = '49b4cc7895ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_settings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('push_token', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_settings')
    # ### end Alembic commands ###
