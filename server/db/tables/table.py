from db.db import get_db, close_connection
import time

from utils import db_logger

class Table:
    def __init__(self, table: str, attr: list):
        self.table = table
        self.attr = attr
        self.create()

    def create(self):
        conn = get_db()
        conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table} ({', '.join([f'{key} {value}' for key, value, _ in self.attr])})")
        db_logger.info(f'Created table [{self.table}]')
        close_connection()

    def insert(self, **kwargs):
        conn = get_db()
        args = list('' for _ in range(len(self.attr)))
        pkey, pval = None, None
        for key, _, primary in self.attr:
            if primary and not key in kwargs:
                raise ValueError(f'Primary key {key} is missing')
            elif primary:
                pkey, pval = key, kwargs[key]
            args[self.attr.index((key, _, primary))] = kwargs[key]
        to_format = (', '.join([key for key, _, primary in self.attr]), ','.join(['?'] * len(self.attr)), pkey, pval)
        cursor = conn.execute("INSERT INTO games ({0}) SELECT {1} WHERE NOT EXISTS (SELECT 1 FROM games WHERE {2} = {3})".format(*to_format), args)
        row = cursor.fetchall()
        db_logger.info(f'Inserted into table [{self.table}] object [{pval}]')
        close_connection()

    def select(self, where, cols='*', order='id', limit=10):
        conn = get_db()
        cursor = conn.execute(f"SELECT {cols} FROM games WHERE {where} ORDER BY {order} LIMIT {limit}")
        result = cursor.fetchall()
        close_connection()
        return result

    def select_all(self):
        conn = get_db()
        time.sleep(10)
        cursor = conn.execute('SELECT * FROM games')
        result = cursor.fetchall()
        close_connection()
        return result
    
    def update(self, where, **kwargs):
        conn = get_db()
        args = list('' for _ in range(len(self.attr)))
        for key, _, primary in self.attr:
            if primary and key in kwargs:
                raise ValueError(f'Cannot update primary key {key}')
            args[self.attr.index((key, _, primary))] = kwargs[key]
        cursor = conn.execute(f"UPDATE games SET {', '.join([f'{key} = ?' for key, _, primary in self.attr])} WHERE {where}", args)
        row = cursor.fetchall()
        db_logger.info(f'Updated table [{self.table}] object [{row[0][0]}]')
        close_connection()
    
    def delete(self, where):
        conn = get_db()
        cursor = conn.execute(f"DELETE FROM games WHERE {where}")
        row = cursor.fetchall()
        db_logger.info(f'Deleted from table [{self.table}] object [{row[0][0]}]')
        close_connection()