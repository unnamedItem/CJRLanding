import sqlite3
import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
db_name = config.get('database', 'name')

class DB:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), f'{db_name}.db')
        self.conn = None

    def connect_db(self):
        self.conn = sqlite3.connect(self.db_path)
    
    def close_db(self):
        self.conn.commit()
        self.conn.close()
