from flask import Blueprint, request, jsonify
import speech_recognition as sr

to_text_bp = Blueprint('audio_routes', __name__)

@to_text_bp.route('/audio-to-text', methods=['POST'])
def audio_a_texto():
    data = request.get_json()
    if 'audio' not in request.files:
        return jsonify({"error": "Ningún audio fue proporcionado"}), 400
    
    archivo_audio = request.files['audio']
    
    if archivo_audio.filename == '':
        return jsonify({"error": "Nombre de archivo no válido"}), 400
    
    audio_a_convertir = data['audio']

    recon = sr.Recognizer()