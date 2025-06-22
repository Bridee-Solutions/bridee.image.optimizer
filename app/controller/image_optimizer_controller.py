from flask import request
import app.service.image_optimizer_service as service

def optimize_image():
    image = request.files["image"]
    service.optimize_image(image)