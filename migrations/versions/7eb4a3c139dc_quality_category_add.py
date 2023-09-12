"""quality category add

Revision ID: 7eb4a3c139dc
Revises: 7c3909979675
Create Date: 2023-02-28 22:33:09.702661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eb4a3c139dc'
down_revision = '7c3909979675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quality', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quality', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###