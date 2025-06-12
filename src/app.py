from flask import Flask
from routes.audio_route import audio_bp
from middlewares.auth import check_api_key

app = Flask(__name__)

app.before_request(check_api_key) # Middleware

app.register_blueprint(audio_bp) # Ruta de audio

app.run(host='0.0.0.0', port=5000, debug=True) # Al desplegar a produccion, cambiar debug a False
