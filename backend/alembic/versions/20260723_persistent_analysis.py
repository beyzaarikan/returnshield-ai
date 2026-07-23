"""persist analysis logs and prediction metadata"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "20260723persist"
down_revision: Union[str, Sequence[str], None] = "cd1aa1028826"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("return_predictions", sa.Column("cart_id", sa.String(), nullable=True))
    op.add_column("return_predictions", sa.Column("analysis_mode", sa.String(), nullable=True))
    op.add_column("return_predictions", sa.Column("score_type", sa.String(), nullable=True))
    op.create_index("ix_return_predictions_cart_id", "return_predictions", ["cart_id"], unique=False)

    op.create_table(
        "agent_logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("cart_id", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("risk_score", sa.Float(), nullable=True),
        sa.Column("risk_level", sa.String(), nullable=True),
        sa.Column("analysis_mode", sa.String(), nullable=True),
        sa.Column("data_source", sa.String(), nullable=True),
        sa.Column("agents_used", sa.Text(), nullable=True),
        sa.Column("reasons", sa.Text(), nullable=True),
        sa.Column("customer_message", sa.Text(), nullable=True),
        sa.Column("merchant_action", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_agent_logs_id", "agent_logs", ["id"], unique=False)
    op.create_index("ix_agent_logs_cart_id", "agent_logs", ["cart_id"], unique=False)
    op.create_index("ix_agent_logs_created_at", "agent_logs", ["created_at"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_agent_logs_created_at", table_name="agent_logs")
    op.drop_index("ix_agent_logs_cart_id", table_name="agent_logs")
    op.drop_index("ix_agent_logs_id", table_name="agent_logs")
    op.drop_table("agent_logs")
    op.drop_index("ix_return_predictions_cart_id", table_name="return_predictions")
    op.drop_column("return_predictions", "score_type")
    op.drop_column("return_predictions", "analysis_mode")
    op.drop_column("return_predictions", "cart_id")
