from flask import Flask, render_template
from flask_cors import CORS

from utils import config
from api.routes import api

def create_app():
    # -----------------------------------
    # Flask app cofig
    app = Flask(
        __name__,
        static_folder=config.get('server', 'static_folder'),
        template_folder=config.get('server', 'template_folder'),
        static_url_path='/static'
    )
    
    # -----------------------------------
    # CORS
    CORS(app)

    # -----------------------------------
    # Serve Vue app
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def index(path):
        return render_template("index.html")
    
    # -----------------------------------
    # API
    app.register_blueprint(api)

    return app