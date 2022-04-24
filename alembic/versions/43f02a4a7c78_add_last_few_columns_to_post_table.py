"""add last few columns to post table

Revision ID: 43f02a4a7c78
Revises: 383547d905b5
Create Date: 2022-04-24 16:02:47.822564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43f02a4a7c78'
down_revision = '383547d905b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
