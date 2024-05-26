import sqlite3
import os

from utils import db_logger, config

db_name = config.get('database', 'name')
db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), f'{db_name}.db'))

class DB:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), f'{db_name}.db')
        self.conn = db_connection
        self.log = db_logger

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Exception as e:
            self.log.error(f'Failed to connect to db [{db_name}]: {e}')
    
    def close_db(self):
        self.conn.commit()
        self.conn.close()
