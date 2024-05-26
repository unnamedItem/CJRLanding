from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from api.games.routes import bp as games

api.register_blueprint(games)