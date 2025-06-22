from flask import Blueprint
from app.controller import image_optimizer_controller as controller

image_optimizer_blueprint = Blueprint("optimizer", __name__)

@image_optimizer_blueprint.route("/optimize", methods=["POST"])
def optimize():
    return controller.optimize_image()