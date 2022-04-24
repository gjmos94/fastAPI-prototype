"""add foreign-key to posts table

Revision ID: 383547d905b5
Revises: 18f44c29b386
Create Date: 2022-04-24 15:37:24.217367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '383547d905b5'
down_revision = '18f44c29b386'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
