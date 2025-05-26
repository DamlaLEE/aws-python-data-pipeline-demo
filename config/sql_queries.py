create_db_sql = "CREATE DATABASE IF NOT EXISTS logistics_project;"

create_customer_table_sql = """
CREATE TABLE IF NOT EXISTS op_customer_table(
    customer_id VARCHAR(20) PRIMARY KEY,
    phone VARCHAR(25),
    country VARCHAR(50),
    address VARCHAR(300),
    level_royalty VARCHAR(20)
);
"""

create_product_table_sql = """
CREATE TABLE IF NOT EXISTS op_product_table(
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(150),
    price DECIMAL(10,2),
    weight_kg DECIMAL(10,2),
    seller_company VARCHAR(100)      
);
"""

create_order_table_sql = """
CREATE TABLE IF NOT EXISTS op_order_table(
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    delivery_id VARCHAR(20),
    delivery_fee DECIMAL(10,2),
    product_id VARCHAR(20),
    order_date TIMESTAMP,
    shipping_date TIMESTAMP,
    request VARCHAR(250),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES op_customer_table(customer_id),
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES op_product_table(product_id)
);
"""
alt_customer_table_sql = """
ALTER TABLE op_customer_table
MODIFY COLUMN customer_id VARCHAR(20) NOT NULL;
"""
alt_product_table_sql = """
ALTER TABLE op_product_table
MODIFY COLUMN product_id VARCHAR(20) NOT NULL;
"""
alt_order_table_sql_1 = """
ALTER TABLE op_order_table
MODIFY COLUMN order_id VARCHAR(20) NOT NULL;
"""

alt_order_table_sql_2 = """
ALTER TABLE op_order_table
MODIFY COLUMN customer_id VARCHAR(20) NOT NULL;
"""

alt_order_table_sql_3 = """
ALTER TABLE op_order_table
MODIFY COLUMN product_id VARCHAR(20) NOT NULL;
"""

insert_customer_table_sql = """
INSERT INTO op_customer_table (customer_id, phone, country, address, level_royalty)
    VALUES (%s, %s, %s, %s, %s);
"""
insert_product_table_sql = """
INSERT INTO op_product_table (product_id, product_name, price, weight_kg, seller_company)
    VALUES (%s, %s, %s, %s, %s);  
"""
insert_order_table_sql = """
INSERT INTO op_order_table (order_id, customer_id, product_id, delivery_id, delivery_fee, order_date, shipping_date, request)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""