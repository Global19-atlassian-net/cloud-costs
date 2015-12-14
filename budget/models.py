from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Float,
    Index,
    Integer,
    Text,
    String
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class AwsDetailedLineItem(Base):
    __tablename__ = 'aws_detailed_line_item'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    product_name = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    subscription_id = Column(Integer, nullable=True)
    pricing_plan_id = Column(Integer, nullable=True)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(64), nullable=True)
    reserved_instance = Column(Boolean, nullable=False)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    blended_cost = Column(Float, nullable=True)
    unblended_rate = Column(Float, nullable=True)
    unblended_cost = Column(Float, nullable=True)
    resource_id = Column(String(64), nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsInvoiceLineItem(Base):
    __tablename__ = 'aws_invoice_line_item'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    product_name = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    subscription_id = Column(Integer, nullable=True)
    pricing_plan_id = Column(Integer, nullable=True)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(64), nullable=True)
    reserved_instance = Column(Boolean, nullable=False)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    blended_cost = Column(Float, nullable=True)
    unblended_rate = Column(Float, nullable=True)
    unblended_cost = Column(Float, nullable=True)
    resource_id = Column(String(64), nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsCostAllocation(Base):
    __tablename__ = 'aws_cost_allocation'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(String(255), nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    billing_period_start_date = Column(DateTime, nullable=False)
    billing_period_end_date = Column(DateTime, nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    payer_account_name = Column(String(255), nullable=False)
    linked_account_name = Column(String(255), nullable=False)
    taxation_address = Column(String(255), nullable=False)
    payer_po_number = Column(Integer, nullable=False)
    product_code = Column(String(64), nullable=False)
    product_name = Column(String(255), nullable=True)
    seller_of_record = Column(String(255), nullable=False)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    currency_code = Column(String(8), nullable=False)
    cost_before_tax = Column(Float, nullable=True)
    credits = Column(Float, nullable=True)
    tax_amount = Column(Float, nullable=True)
    tax_type = Column(String(255), nullable=False)
    total_cost = Column(Float, nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsLinkedAccountId(Base):
    __tablename__ = 'aws_linked_account_id'

    id = Column(Integer, primary_key=True)
    linked_account_id = Column(String(255), nullable=True, unique=True)
    account_name = Column(String(255), nullable=True)

class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    fiscal_year = Column(Integer, nullable=False)
    quarter = Column(Integer, nullable=False)
    qtr_start = Column(DateTime, nullable=False)
    qtr_end = Column(DateTime, nullable=False)
    budget = Column(Float, nullable=False)

class MiscExpenses(Base):
    __tablename__ = 'misc_expenses'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    vendor = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    amortizable = Column(Integer, nullable=True)

class NodeCapacity(Base):
    __tablename__ = 'node_capacity'

    id = Column(Integer, primary_key=True)
    node_type = Column(String(255), nullable=False)
    active_capacity = Column(Integer, nullable=True)

class OpenshiftProfileStats(Base):
    __tablename__ = 'openshift_profile_stats'

    id = Column(Integer, primary_key=True)
    collection_date = Column(DateTime, nullable=False)
    profile_name = Column(String(255), nullable=False)
    nodes_count = Column(Integer, nullable=True)
    gears_active_count = Column(Integer, nullable=True)
    gears_idle_count = Column(Integer, nullable=True)
    gears_stopped_count = Column(Integer, nullable=True)
    gears_unknown_count = Column(Integer, nullable=True)
    gears_total_count = Column(Integer, nullable=True)

#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)
#
#Index('my_index', MyModel.name, unique=True, mysql_length=255)
