from flask import Flask
from routes.to_audio_route import to_audio_bp
from routes.to_text_route import to_text_bp
from middlewares.auth import check_api_key

app = Flask(__name__)

app.before_request(check_api_key) # Middleware

app.register_blueprint(to_audio_bp) # Ruta de tts
app.register_blueprint(to_text_bp) # Ruta de stt

app.run(host='0.0.0.0', port=5000, debug=True) # Al desplegar a produccion, cambiar debug a False
