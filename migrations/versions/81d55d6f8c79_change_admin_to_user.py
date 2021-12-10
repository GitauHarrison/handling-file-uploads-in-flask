"""change admin to user

Revision ID: 81d55d6f8c79
Revises: e7a88735908f
Create Date: 2021-12-10 16:15:56.530320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d55d6f8c79'
down_revision = 'e7a88735908f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('avatar', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('ix_admin_email', table_name='admin')
    op.drop_index('ix_admin_username', table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('about_me', sa.VARCHAR(length=140), nullable=True),
    sa.Column('avatar', sa.VARCHAR(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_admin_username', 'admin', ['username'], unique=False)
    op.create_index('ix_admin_email', 'admin', ['email'], unique=False)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###