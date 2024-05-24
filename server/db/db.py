import sqlite3
import os
from configparser import ConfigParser

from logger import setup_logger

config = ConfigParser()
config.read('config.ini')
db_name = config.get('database', 'name')


class DB:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), f'{db_name}.db')
        self.conn = None
        self.log = setup_logger('db')

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Exception as e:
            self.log.error(f'Failed to connect to db [{db_name}]: {e}')
    
    def close_db(self):
        self.conn.commit()
        self.conn.close()
