from dotenv import load_dotenv
from app import create_app
import os

load_dotenv()
PORT = int(os.getenv('PORT', 8080))
IS_DEBUG = os.getenv('DEBUG', 'False').lower() == "true"

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=IS_DEBUG)