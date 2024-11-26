"""add few last columns to posts table

Revision ID: 6975fd45126f
Revises: b32ba82d36b1
Create Date: 2024-11-25 15:23:25.187411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6975fd45126f'
down_revision: Union[str, None] = 'b32ba82d36b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
 op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False))
 op.add_column("posts", sa.Column("published", sa.Boolean(), server_default="TRUE", nullable=False))

                          
def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
