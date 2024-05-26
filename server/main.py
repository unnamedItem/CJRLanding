from app import create_app
from utils import server_logger, config 

# @app.route("/", defaults={"path": ""})
# @app.route("/<path:path>")
# def index(path):
#     return render_template("index.html")

if __name__ == '__main__':
    server_logger.info('Starting server...')
    server_logger.info('Server started at http://{}:{}'.format(config.get('server', 'host'), config.get('server', 'port')))
    app = create_app()
    app.run(debug=True, host=config.get('server', 'host'), port=config.get('server', 'port'))
    server_logger.info('Server stopped')