import pymysql
import yaml
import pandas as pd

class DBManager:
    def __init__(self, path='config/db_info.yml', database=None):
        self.config = self.load_db_config(path, database)

    def load_db_config(self, path, database):
        try:
            with open(path,'r') as file:
                config = yaml.safe_load(file)['db_info']
            if database:
                config['database'] = database
            return config
        except FileNotFoundError: 
            raise FileNotFoundError(f"Cannot find config file at: {path}")
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error: {e}") # 데이터 구조가 잘못된 경우
        

    def execute_sql(self, sql):
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
        except pymysql.MySQLError as e:
            print(f"SQL error: \n{sql}\n error: {e}")
            raise
        finally:
            connection.close()
    

    def insert_data(self, sql, data):
        if not data:
            print("There is no data for insert")
            return
        
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                cursor.executemany(sql, data)
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"Error comes up for insert:\n{sql}\n error: {e}")
            raise
        finally:
            connection.close()
        
    def fetch_table(self, table_name):
        connection = pymysql.connect(**self.config)
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name};", connection)
            return df
        except Exception as e:
            print(f"Faile to call up those tables: {table_name}\n error: {e}")
            raise
        finally:
            connection.close()
    
    def make_dataframe(self, sql):
        connection = pymysql.connect(**self.config)
        try:
            rows = pd.read_sql(sql, connection)
            df = pd.DataFrame(rows)
            return df
        finally:
            connection.close()
