"""added apikey

Revision ID: ec6cf07ff68a
Revises: cda6903dfc0c
Create Date: 2022-09-19 21:04:37.967466

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = "ec6cf07ff68a"
down_revision = "cda6903dfc0c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "api_keys",
        sa.Column("key", sa.String(length=48), nullable=False),
        sa.Column("user", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.ForeignKeyConstraint(["user"], ["users.id"], name="fk_api_keys_users_id_user"),
        sa.PrimaryKeyConstraint("key"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("api_keys")
    # ### end Alembic commands ###
