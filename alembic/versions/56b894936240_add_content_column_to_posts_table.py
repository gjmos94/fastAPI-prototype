"""add content column to posts table

Revision ID: 56b894936240
Revises: dde75aefc135
Create Date: 2022-04-24 15:10:09.284063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b894936240'
down_revision = 'dde75aefc135'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
