"""added unit to the lab test model

Revision ID: dfa587efe305
Revises: ba471631a84d
Create Date: 2024-09-30 05:56:55.438256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfa587efe305'
down_revision = 'ba471631a84d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_tests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unit', sa.String(), nullable=True))

    with op.batch_alter_table('lab_tests_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unit', sa.String(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_tests_version', schema=None) as batch_op:
        batch_op.drop_column('unit')

    with op.batch_alter_table('lab_tests', schema=None) as batch_op:
        batch_op.drop_column('unit')

    # ### end Alembic commands ###
