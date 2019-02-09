"""empty message

Revision ID: 82e1b8ed0b6e
Revises: 
Create Date: 2019-02-09 19:05:06.449300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e1b8ed0b6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('presence',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('enter', sa.DateTime(), nullable=True),
    sa.Column('exit', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('rights', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('presence')
    # ### end Alembic commands ###