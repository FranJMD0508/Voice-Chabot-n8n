from flask import request, jsonify
from config import Config

def check_api_key():
    api_key_recibida = request.headers.get("API-KEY")
    if not api_key_recibida or api_key_recibida != Config.API_KEY:
        return jsonify({"error": "No Autorizado: Api Key no válida"}), 401