"""create participants table

Revision ID: 08f870cfb0b8
Revises: a2b8e076eb2b
Create Date: 2023-05-20 14:55:26.017389

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "08f870cfb0b8"
down_revision = "a2b8e076eb2b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "participants",
        sa.Column("participant_id", sa.BigInteger(), primary_key=True),
        sa.Column("external_id", sa.UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column("meeting_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("greetings", sa.CHAR(length=64), nullable=False),
        sa.ForeignKeyConstraint(("meeting_id",), ("meetings.meeting_id",)),
        sa.ForeignKeyConstraint(("user_id",), ("users.user_id",)),
    )


def downgrade() -> None:
    op.drop_table("participants")
