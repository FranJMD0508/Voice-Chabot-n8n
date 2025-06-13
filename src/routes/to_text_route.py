from flask import Blueprint, request, jsonify
import speech_recognition as sr
from middlewares.audio_processing import procesar_archivo_audio
from services.conversion_stt import conversion_audio_a_texto

to_text_bp = Blueprint('text_routes', __name__)

@to_text_bp.route('/audio-to-text', methods=['POST'])
def audio_a_texto():

    if 'audio' not in request.files:
        return jsonify({"error": "Ningún audio fue proporcionado"}), 400
    
    archivo_audio = request.files['audio']
    
    if archivo_audio.filename == '':
        return jsonify({"error": "Nombre de archivo no válido"}), 400

    try:
        processed_wav_stream = procesar_archivo_audio(archivo_audio)
        print("Audio preprocesado a WAV en memoria.")

    except Exception as e:
        print(f"Error al preprocesar el archivo de audio: {e}")
        return jsonify({"error": f"Error al procesar el archivo de audio: {e}."}), 400
    
    try:
        texto = conversion_audio_a_texto(processed_wav_stream)
        return jsonify({"transcripcion": texto}), 200
    
    except sr.UnknownValueError:
        print("SpeechRecognition no pudo entender el audio.")
        return jsonify({"error": "No se pudo entender el audio. Podría ser ruido o habla no clara."}), 400
    except sr.RequestError as e:
        print(f"Error al conectar con el servicio de Google: {e}")
        return jsonify({"error": f"Error al conectar con el servicio de Google. Asegúrate de tener conexión a internet. Detalle: {e}"}), 500
    except Exception as e:
        print(f"Error inesperado durante la transcripción: {e}")
        return jsonify({"error": f"Error inesperado durante la transcripción: {e}"}), 500
