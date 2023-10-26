"""redesigned models so that a customer can have many orders each of which can also has multiple tests

Revision ID: a9f858682547
Revises: e670d6e99921
Create Date: 2023-10-27 01:25:51.873669

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a9f858682547'
down_revision = 'e670d6e99921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lab_test_records_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('num_result', sa.Numeric(), autoincrement=False, nullable=True),
    sa.Column('text_result', sa.String(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.Text(), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('cancelled', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('updator_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('test_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('order_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    with op.batch_alter_table('lab_test_records_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_lab_test_records_version_end_transaction_id'), ['end_transaction_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_lab_test_records_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_lab_test_records_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('lab_tests_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(), autoincrement=False, nullable=False),
    sa.Column('detail', sa.Text(), autoincrement=False, nullable=True),
    sa.Column('min_value', sa.Numeric(), autoincrement=False, nullable=True),
    sa.Column('max_value', sa.Numeric(), autoincrement=False, nullable=True),
    sa.Column('min_ref_value', sa.Numeric(), autoincrement=False, nullable=True),
    sa.Column('max_ref_value', sa.Numeric(), autoincrement=False, nullable=True),
    sa.Column('choice_set', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('active', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('added_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('lab_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('data_type', sa.String(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    with op.batch_alter_table('lab_tests_version', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_lab_tests_version_end_transaction_id'), ['end_transaction_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_lab_tests_version_operation_type'), ['operation_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_lab_tests_version_transaction_id'), ['transaction_id'], unique=False)

    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lab_test_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lab_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('ordered_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ordered_by_id', sa.Integer(), nullable=True),
    sa.Column('cancelled_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('reject_record_id', sa.Integer(), nullable=True),
    sa.Column('received_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('approved_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('approver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['approver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['lab_customers.id'], ),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], ),
    sa.ForeignKeyConstraint(['ordered_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['reject_record_id'], ['lab_order_reject_records.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lab_tests',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.Column('min_value', sa.Numeric(), nullable=True),
    sa.Column('max_value', sa.Numeric(), nullable=True),
    sa.Column('min_ref_value', sa.Numeric(), nullable=True),
    sa.Column('max_ref_value', sa.Numeric(), nullable=True),
    sa.Column('choice_set', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('added_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('lab_id', sa.Integer(), nullable=True),
    sa.Column('data_type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['choice_set'], ['lab_result_choice_set.id'], ),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lab_test_records',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('num_result', sa.Numeric(), nullable=True),
    sa.Column('text_result', sa.String(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cancelled', sa.Boolean(), nullable=True),
    sa.Column('updator_id', sa.Integer(), nullable=True),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['lab_test_orders.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['lab_tests.id'], ),
    sa.ForeignKeyConstraint(['updator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('lab_quan_result_records')
    op.drop_table('lab_qual_result_records')
    op.drop_table('lab_qual_result_sets')
    op.drop_table('lab_quan_result_sets')
    op.drop_table('lab_quan_test_orders')
    op.drop_table('lab_qual_test_orders')
    op.drop_table('lab_quan_tests')
    op.drop_table('lab_qual_tests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lab_qual_test_orders',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('lab_qual_test_orders_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('lab_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('test_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ordered_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('ordered_by_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cancelled_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('received_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('receiver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('finished_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('reject_record_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('approved_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('approver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['approver_id'], ['user.id'], name='lab_qual_test_orders_approver_id_fkey'),
    sa.ForeignKeyConstraint(['customer_id'], ['lab_customers.id'], name='lab_qual_test_orders_customer_id_fkey'),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], name='lab_qual_test_orders_lab_id_fkey'),
    sa.ForeignKeyConstraint(['ordered_by_id'], ['user.id'], name='lab_qual_test_orders_ordered_by_id_fkey'),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], name='lab_qual_test_orders_receiver_id_fkey'),
    sa.ForeignKeyConstraint(['reject_record_id'], ['lab_order_reject_records.id'], name='lab_qual_test_orders_reject_record_id_fkey'),
    sa.ForeignKeyConstraint(['test_id'], ['lab_qual_tests.id'], name='lab_qual_test_orders_test_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_qual_test_orders_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('lab_qual_result_records',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('record_set_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('text_result', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('cancelled', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('updator_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['record_set_id'], ['lab_qual_result_sets.id'], name='lab_qual_result_records_record_set_id_fkey'),
    sa.ForeignKeyConstraint(['updator_id'], ['user.id'], name='lab_qual_result_records_updator_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_qual_result_records_pkey')
    )
    op.create_table('lab_quan_result_records',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('record_set_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_result', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('text_result', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('cancelled', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('updator_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['record_set_id'], ['lab_quan_result_sets.id'], name='lab_quan_result_records_record_set_id_fkey'),
    sa.ForeignKeyConstraint(['updator_id'], ['user.id'], name='lab_quan_result_records_updator_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_quan_result_records_pkey')
    )
    op.create_table('lab_qual_tests',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('lab_qual_tests_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('detail', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('choice_set', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('added_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('lab_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['choice_set'], ['lab_result_choice_set.id'], name='lab_qual_tests_choice_set_fkey'),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], name='lab_qual_tests_lab_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_qual_tests_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('lab_quan_tests',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('lab_quan_tests_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('detail', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('min_value', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('max_value', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('min_ref_value', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('max_ref_value', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('choice_set', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('added_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('lab_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['choice_set'], ['lab_result_choice_set.id'], name='lab_quan_tests_choice_set_fkey'),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], name='lab_quan_tests_lab_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_quan_tests_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('lab_quan_test_orders',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('lab_quan_test_orders_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('lab_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('test_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ordered_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('ordered_by_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cancelled_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('received_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('receiver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('finished_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('reject_record_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('approved_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('approver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['approver_id'], ['user.id'], name='lab_quan_test_orders_approver_id_fkey'),
    sa.ForeignKeyConstraint(['customer_id'], ['lab_customers.id'], name='lab_quan_test_orders_customer_id_fkey'),
    sa.ForeignKeyConstraint(['lab_id'], ['labs.id'], name='lab_quan_test_orders_lab_id_fkey'),
    sa.ForeignKeyConstraint(['ordered_by_id'], ['user.id'], name='lab_quan_test_orders_ordered_by_id_fkey'),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], name='lab_quan_test_orders_receiver_id_fkey'),
    sa.ForeignKeyConstraint(['reject_record_id'], ['lab_order_reject_records.id'], name='lab_quan_test_orders_reject_record_id_fkey'),
    sa.ForeignKeyConstraint(['test_id'], ['lab_quan_tests.id'], name='lab_quan_test_orders_test_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_quan_test_orders_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('lab_quan_result_sets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['lab_quan_test_orders.id'], name='lab_quan_result_sets_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_quan_result_sets_pkey')
    )
    op.create_table('lab_qual_result_sets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['lab_qual_test_orders.id'], name='lab_qual_result_sets_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='lab_qual_result_sets_pkey')
    )
    op.drop_table('lab_test_records')
    op.drop_table('lab_tests')
    op.drop_table('lab_test_orders')
    op.drop_table('transaction')
    with op.batch_alter_table('lab_tests_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_lab_tests_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_lab_tests_version_operation_type'))
        batch_op.drop_index(batch_op.f('ix_lab_tests_version_end_transaction_id'))

    op.drop_table('lab_tests_version')
    with op.batch_alter_table('lab_test_records_version', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_lab_test_records_version_transaction_id'))
        batch_op.drop_index(batch_op.f('ix_lab_test_records_version_operation_type'))
        batch_op.drop_index(batch_op.f('ix_lab_test_records_version_end_transaction_id'))

    op.drop_table('lab_test_records_version')
    # ### end Alembic commands ###
