import io
from pydub import AudioSegment

def procesar_archivo_audio(audio_file):
    audio_bytes_io = io.BytesIO(audio_file.read())

    audio_segment = AudioSegment.from_file(audio_bytes_io)
    audio_segment = audio_segment.set_channels(1)      # Convertir a mono
    audio_segment = audio_segment.set_frame_rate(16000) # Establecer a 16 kHz

    # Crear un stream de bytes en memoria para el audio procesado
    processed_audio_stream = io.BytesIO()
    audio_segment.export(processed_audio_stream, format="wav")
    processed_audio_stream.seek(0) # Mover el puntero al inicio del stream