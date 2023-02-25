from flask import Flask

def make_app(secret_key: str, instance_path: str) -> Flask:
    app = Flask(__name__)

    app.secret_key = secret_key
    app.instance_path = instance_path

    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    return app