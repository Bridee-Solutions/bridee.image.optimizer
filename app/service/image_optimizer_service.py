import os.path
from tempfile import NamedTemporaryFile
from werkzeug.datastructures import FileStorage
from PIL import Image
from werkzeug.utils import send_file

def optimize_image(image: FileStorage):
    with NamedTemporaryFile(suffix=os.path.splitext(image.filename)[1], delete=False) as tmp_file:
        image.save(tmp_file)
        tmp_file_path = tmp_file.name
        optimize(tmp_file_path)

    return send_file(tmp_file_path, mimetype="application/octet-stream", as_attachment=True,
                     download_name=image.filename)


def optimize(file_name: str):
    try:
        with Image.open(file_name) as img:
            img.save(
                file_name,
                file_name.split(".")[1],
                optimize=True,
                compress_level=6
            )
        print("Imagem otimizada com sucesso!")
    except Exception as exception:
        print("O seguinte erro ocorreu ao tentar otimizar a imagem:")
        print(f"{exception}")
        print(f"Stderr: {exception.stderr.decode()}")