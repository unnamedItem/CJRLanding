from configparser import ConfigParser

from flask import Flask, render_template, jsonify
from flask_cors import CORS

config = ConfigParser()
config.read('config.ini')

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
    return jsonify({'hello': 'world'})

if __name__ == '__main__':
    app.run(debug=True, host=config.get('server', 'host'), port=config.get('server', 'port'))