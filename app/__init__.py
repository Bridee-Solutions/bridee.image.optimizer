from flask import Flask
from app.route.image_optimizer_route import image_optimizer_blueprint

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(image_optimizer_blueprint, url_prefix="/api")

    return app