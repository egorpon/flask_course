"""added breed column

Revision ID: 40ca2b66be31
Revises: 
Create Date: 2025-03-04 18:58:13.991191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40ca2b66be31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('breed', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppy', schema=None) as batch_op:
        batch_op.drop_column('breed')

    # ### end Alembic commands ###
