from configparser import ConfigParser

import xmltodict
import requests
from flatten_json import flatten

from db.tables.table import Table

config = ConfigParser()
config.read('config.ini')

GAME_ATTRIBUTES = [
    ('id', 'INTEGER PRIMARY KEY', True),
    ('name', 'TEXT NOT NULL', False),
    ('description', 'TEXT NOT NULL', False),
    ('yearpublished', 'INTEGER', False),
    ('minplayers', 'INTEGER', False),
    ('maxplayers', 'INTEGER', False),
    ('minplaytime', 'INTEGER', False),
    ('maxplaytime', 'INTEGER', False),
    ('age', 'INTEGER', False),
    ('thumbnail', 'TEXT', False),
    ('image', 'TEXT', False),
    ('averageweight', 'FLOAT', False),
    ('average', 'FLOAT', False),
    ('boardgamemechanic', 'TEXT', False),
    ('boardgamesubdomain', 'TEXT', False),
    ('boardgamecategory', 'TEXT', False),
    ('boardgamedesigner', 'TEXT', False),
    ('boardgamepublisher', 'TEXT', False),
]

class Games(Table):
    def __init__(self):
        self.collection = config.get('bgg', 'collection')
        self.collection_url = f"{config.get('bgg', 'api_url')}/collection/{self.collection}"
        super().__init__('games', GAME_ATTRIBUTES)
        self.create()
        self.get_bgg()

    def get_bgg(self, forced=False):
        game_ids = self.get_collection()
        for id in game_ids:
            already_exists = self.select('id', f"id = {id}") and not forced
            not already_exists and self.get_game(id)

    def get_collection(self):
        response = requests.get(self.collection_url)
        if response.status_code == 200:
            data = xmltodict.parse(response.text)
            flat = list(map(lambda item: flatten(item), data['items']['item']))
            ids = list(map(lambda item: item['@objectid'], flat))
            return ids
    
    def get_game(self, id):
        url = f"{config.get('bgg', 'api_url')}/boardgame/{id}?stats=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = xmltodict.parse(response.text)
            flat = flatten(data['boardgames']['boardgame'], separator='.')

            def check_attr(attr, key, type):
                keys = key.split('.')
                if attr == key:
                    return True
                elif 'TEXT' in type:
                    return attr in keys and '#text' in keys
                return attr in keys
            
            def parse_attr(value, type):
                if 'PRIMARY KEY' in type:
                    return id
                elif 'TEXT' in type:
                    return str(value)
                elif 'INTEGER' in type:
                    return int(value)
                elif 'FLOAT' in type:
                    return float(value)
                return value

            def get_attr(attr, type):
                return parse_attr(', '.join([value for key, value in flat.items() if check_attr(attr, key, type)]), type)

            kwargs = {attr: get_attr(attr, type) for attr, type, _ in self.attr}
            self.insert(**kwargs)
            
        