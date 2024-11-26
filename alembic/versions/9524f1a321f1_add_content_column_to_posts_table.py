"""add content column to posts table

Revision ID: 9524f1a321f1
Revises: bc873f0b1dd8
Create Date: 2024-11-25 14:50:06.762625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9524f1a321f1'
down_revision: Union[str, None] = 'bc873f0b1dd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
