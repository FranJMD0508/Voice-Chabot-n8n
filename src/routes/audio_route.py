from flask import Blueprint, request, send_file, jsonify
from services.conversion_tts import conversion_texto_a_audio

audio_bp = Blueprint('audio_routes', __name__)

@audio_bp.route('/text-to-audio', methods=['POST'])
def texto_a_audio():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Ningún texto fue proporcionado"}), 400
    
    texto_a_convertir = data['text']
    idioma = data.get('lang', 'es')

    try:
        audio_stream = conversion_texto_a_audio(texto_a_convertir, idioma)
        return send_file(audio_stream, mimetype='audio/mpeg', as_attachment=True, download_name='audio.mp3')
    
    except Exception as e:
        print(f"Error al convertir el texto a audio: {e}")
        return jsonify({"error": "Falló la conversión", "detalles": str(e)}), 500