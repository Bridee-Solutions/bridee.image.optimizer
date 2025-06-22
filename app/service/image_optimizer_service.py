import os.path
from tempfile import NamedTemporaryFile

from flask import send_file, Response
from werkzeug.datastructures import FileStorage
from PIL import Image

def optimize_image(image: FileStorage) -> Response:
    with NamedTemporaryFile(suffix=os.path.splitext(image.filename)[1], delete=False) as tmp_file:
        image.save(tmp_file)
        tmp_file_path = tmp_file.name
        optimize(tmp_file_path)

    return send_file(tmp_file_path, mimetype="image/*", as_attachment=True,
                     download_name=image.filename)


def optimize(file_name: str):
    file_extension = file_name.split(".")[1]
    file_extension = "JPEG" if file_extension.lower().__eq__("jpg") else file_extension.upper()
    try:
        with Image.open(file_name) as img:
            img.save(
                file_name,
                file_extension,
                optimize=True,
                compress_level=6
            )
        print("Imagem otimizada com sucesso!")
    except Exception as exception:
        print("O seguinte erro ocorreu ao tentar otimizar a imagem:")
        print(f"{exception}")