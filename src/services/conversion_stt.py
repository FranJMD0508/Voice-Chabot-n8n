import speech_recognition as sr

def conversion_audio_a_texto(processed_wav_stream, idioma='es'):
    recon = sr.Recognizer()

    with sr.AudioFile(processed_wav_stream) as source:
        audio_data = recon.record(source)

    texto = recon.recognize_google(audio_data, language=idioma) 
    
    return texto
    
