import mariadb
import sys

class MariaDBManager:
    def __init__(self, db_user, db_password, db_host, db_port, db_name=None):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def _connect(self, database=None):
        try:
            conn = mariadb.connect(
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=int(self.db_port),
                database=database
            )
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def create_database(self, dbname):
        conn = self._connect()
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE DATABASE {dbname}")
            print(f"Database {dbname} created successfully")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def create_table(self, table_name):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT
                )
            """)
            print(f"Table {table_name} created successfully")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def insert_data(self, table_name, name, age):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            cur.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", (name, age))
            conn.commit()
            print(f"Data inserted successfully into {table_name}")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def select_data(self, table_name):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def update_data(self, table_name, record_id, name=None, age=None):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            if name and age:
                cur.execute(f"UPDATE {table_name} SET name=?, age=? WHERE id=?", (name, age, record_id))
            elif name:
                cur.execute(f"UPDATE {table_name} SET name=? WHERE id=?", (name, record_id))
            elif age:
                cur.execute(f"UPDATE {table_name} SET age=? WHERE id=?", (age, record_id))
            conn.commit()
            print(f"Data updated successfully in {table_name}")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def delete_data(self, table_name, record_id):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE id=?", (record_id,))
            conn.commit()
            print(f"Data deleted successfully from {table_name}")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def drop_table(self, table_name):
        conn = self._connect(self.db_name)
        cur = conn.cursor()
        try:
            cur.execute(f"DROP TABLE IF EXISTS {table_name}")
            print(f"Table {table_name} dropped successfully")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def drop_database(self, dbname):
        conn = self._connect()
        cur = conn.cursor()
        try:
            cur.execute(f"DROP DATABASE IF EXISTS {dbname}")
            print(f"Database {dbname} dropped successfully")
        except mariadb.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()
