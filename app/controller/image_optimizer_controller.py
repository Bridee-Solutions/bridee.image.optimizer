from flask import request, Response
import app.service.image_optimizer_service as service

def optimize_image() -> Response:
    image = request.files["image"]
    return service.optimize_image(image)