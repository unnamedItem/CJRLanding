import sqlite3
import os

from flask import g

from utils import config

DB_NAME = config.get('database', 'name')
DB_PATH = os.path.join(os.path.dirname(__file__), f'{DB_NAME}.db')

db = {}


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = make_dicts
    return db

def close_connection():
    db = getattr(g, '_database', None)
    if db is not None:
        db.commit()
        db.close()

def init_db():
    import db.tables as tables
    db['games'] = tables.Games()