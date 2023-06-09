"""create meetings table

Revision ID: a2b8e076eb2b
Revises: 4ebc732af0cd
Create Date: 2023-05-20 14:51:38.287592

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a2b8e076eb2b"
down_revision = "4ebc732af0cd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "meetings",
        sa.Column("meeting_id", sa.UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("title", sa.CHAR(length=128), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("meetings")
