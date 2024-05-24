import xmltodict
import json
from configparser import ConfigParser

import requests
from flask import Flask, render_template, jsonify
from flask_cors import CORS

from db.tables.games import Games
from logger import setup_logger

config = ConfigParser()
config.read('config.ini')

log = setup_logger('server')

app = Flask(
    __name__,
    static_folder=config.get('server', 'static_folder'),
    template_folder=config.get('server', 'template_folder'),
    static_url_path='/static')
CORS(app)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

@app.route('/api')
def get():
    url = 'https://boardgamegeek.com/xmlapi/boardgame/2860?stats=1'
    response = requests.get(url)

    if response.status_code == 200:
        data_dict = xmltodict.parse(response.text)
        json_data = json.dumps(data_dict, indent=4)
        return jsonify(json_data)
    else:
        return jsonify({'error': 'Failed to fetch boardgame data'}), response.status_code

if __name__ == '__main__':
    games = Games()
    log.info('Starting server...')
    log.info('Server started at http://{}:{}'.format(config.get('server', 'host'), config.get('server', 'port')))
    app.run(debug=True, host=config.get('server', 'host'), port=config.get('server', 'port'))
    log.info('Server stopped')