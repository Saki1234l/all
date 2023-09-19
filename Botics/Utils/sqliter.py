import sqlite3

class SQLiteDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        try:
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(create_table_query)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating table: {str(e)}")
            return False

    def insert_data(self, table_name, data):
        try:
            placeholders = ', '.join(['?' for _ in data])
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(insert_query, data)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting data: {str(e)}")
            return False

    def fetch_data(self, table_name, condition=None):
        try:
            select_query = f"SELECT * FROM {table_name}"
            if condition:
                select_query += f" WHERE {condition}"
            self.cursor.execute(select_query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return []

    def delete_data(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(delete_query)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting data: {str(e)}")
            return False

    def close_connection(self):
        self.conn.close()
