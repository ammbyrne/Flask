"""empty message

Revision ID: 08aa5333fa0f
Revises: a4c6516b301b
Create Date: 2017-09-18 08:35:49.536774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08aa5333fa0f'
down_revision = 'a4c6516b301b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=140), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    # ### end Alembic commands ###
