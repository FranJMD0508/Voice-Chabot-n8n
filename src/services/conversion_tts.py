from gtts import gTTS
import io

def conversion_texto_a_audio(texto: str, idioma: str = 'es') -> io.BytesIO:
    print(f"Convirtiendo a audio: '{texto[:50]}...' en: {idioma}")

    tts = gTTS(text=texto, lang=idioma, slow=False)
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    return audio_stream