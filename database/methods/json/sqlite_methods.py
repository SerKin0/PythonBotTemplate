import sqlite3


class SQLiteDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        # Метод для создания таблицы
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert_data(self, table_name, data):
        # Метод для добавления данных в таблицу
        placeholders = ', '.join('?' * len(data))
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
        self.conn.commit()

    def update_data(self, table_name, new_data, condition):
        # Метод для обновления данных
        self.cursor.execute(f"UPDATE {table_name} SET {new_data} WHERE {condition}")
        self.conn.commit()

    def delete_data(self, table_name: str, condition: str):
        # Метод для удаления данных
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def select_data(self, table_name, columns, condition=None):
        # Метод для выборки данных
        if condition:
            self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        else:
            self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def close_connection(self):
        # Метод для закрытия соединения с базой данных
        self.conn.close()
