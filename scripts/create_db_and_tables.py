#import pymysql
from utils.db_helper import DBManager
from config.sql_queries import (
    create_db_sql,
    create_customer_table_sql,
    create_product_table_sql,
    create_order_table_sql,
    alt_customer_table_sql,
    alt_product_table_sql,
    alt_order_table_sql_1,
    alt_order_table_sql_2,
    alt_order_table_sql_3,
    insert_customer_table_sql,
    insert_order_table_sql,
    insert_product_table_sql
)
from data.initial_data import (
    customer_data,
    product_data,
    order_data,
    customer_data_additional,
    product_data_additional,
    order_data_additional
)

## 초기화 코드 _ reset
# delete_db_sql = "DROP DATABAS;"
# execute_sql(del')
db = DBManager(path='config/db_info.yml', database='logistics_project')

## 1. CREATE database
def create_database():
    db=DBManager(path='config/db_info.yml', database='mysql')
    db.execute_sql(create_db_sql)

## 2. CREATE tables (customer, product, order)
def create_tables():
    db.execute_sql(create_customer_table_sql)
    db.execute_sql(create_product_table_sql)
    db.execute_sql(create_order_table_sql)

## 3. ALTER tables settings'
def alter_data_bulk(sql):
    db.execute_sql(sql)
## 4. ADD 10 rows
def insert_data_bulk(sql, data):
    db = DBManager(path='config/db_info.yml', database='logistics_project')
    db.insert_data(sql, data)

def run_all():
    create_database()
    create_tables()

if __name__ == "__main__":
    run_all()