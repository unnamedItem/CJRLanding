from db.db import DB

class Table(DB):
    def __init__(self, table: str, attr: list):
        super().__init__()
        self.table = table
        self.attr = attr

    def create(self):
        self.connect_db()
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table} ({', '.join([f'{key} {value}' for key, value, _ in self.attr])})")
        self.close_db()

    def insert(self, **kwargs):
        self.connect_db()
        args = list('' for _ in range(len(self.attr)))
        pkey, pval = None, None
        for key, _, primary in self.attr:
            if primary and not key in kwargs:
                raise ValueError(f'Primary key {key} is missing')
            elif primary:
                pkey, pval = key, kwargs[key]
            args[self.attr.index((key, _, primary))] = kwargs[key]
        to_format = (', '.join([key for key, _, primary in self.attr]), ','.join(['?'] * len(self.attr)), pkey, pval)
        self.conn.execute("INSERT INTO games ({0}) SELECT {1} WHERE NOT EXISTS (SELECT 1 FROM games WHERE {2} = {3})".format(*to_format), args)
        self.close_db()

    def select(self, cols, where, order='id', limit=10):
        self.connect_db()
        cursor = self.conn.execute(f"SELECT {cols} FROM games WHERE {where} ORDER BY {order} LIMIT {limit}")
        result = cursor.fetchall()
        self.close_db()
        return result

    def select_all(self):
        self.connect_db()
        cursor = self.conn.execute('SELECT * FROM games')
        result = cursor.fetchall()
        self.close_db()
        return result
    
    def update(self, where, **kwargs):
        self.connect_db()
        args = list('' for _ in range(len(self.attr)))
        for key, _, primary in self.attr:
            if primary and not key in kwargs:
                raise ValueError(f'Primary key {key} is missing')
            args[self.attr.index((key, _, primary))] = kwargs[key]
        self.conn.execute(f"UPDATE games SET {', '.join([f'{key} = ?' for key, _, primary in self.attr])} WHERE {where}", args)
        self.close_db()
    
    def delete(self, where):
        self.connect_db()
        self.conn.execute(f"DELETE FROM games WHERE {where}")
        self.close_db()