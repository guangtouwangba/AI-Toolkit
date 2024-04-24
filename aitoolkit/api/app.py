from flask import Flask
from flask_restful import Api
from aitoolkit.api.agents import bp as agent_bp
from aitoolkit.api.initialize import initialize_router


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    initialize_router(api)

    return app


if __name__ == '__main__':
    routes = []
    app = create_app()
    print('Available routes:' + '\n' + '-' * 20)
    for route in app.url_map.iter_rules():
        routes.append('%s' % route)
    print('\n'.join(sorted(routes)))
    app.run(port=8080, debug=True)
