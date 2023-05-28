"""create users table

Revision ID: 4ebc732af0cd
Revises: 
Create Date: 2023-05-20 14:47:10.926756

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4ebc732af0cd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("user_id", sa.UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("first_name", sa.CHAR(length=128), nullable=False),
        sa.Column("last_name", sa.CHAR(length=128), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
