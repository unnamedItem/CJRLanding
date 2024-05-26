from flask import Blueprint

from api.games import games

bp = Blueprint('games', __name__, url_prefix='/games')


class GamesHandler:
    @staticmethod
    @bp.route('/<int:id>')
    def get_game(id):
        game = games.select(id)
        return game

    @staticmethod
    @bp.route('/')
    def get_games():
        game_list = games.select_all()
        return game_list