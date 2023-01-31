import speech_recognition as sr
import pyaudio
import time
import datetime
import whisper

class oido:
    def __init__(self):
        self

    def escuchar(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
                if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                        print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

        p.terminate()
        recog = sr.Recognizer()
        mic = sr.Microphone()

        with mic as fuente:
            recog.adjust_for_ambient_noise(fuente)
        print("Escuchando...")
        with mic as fuente:
            audio = recog.listen(fuente, phrase_time_limit=15)
        
        now = datetime.datetime.now()
        nombre_archivo = now.strftime("./files/audio/%Y-%m-%d_%H-%M-%S") + ".wav"

        with open(nombre_archivo, "wb") as f:
            f.write(audio.get_wav_data())

        model = whisper.load_model("base")
        result = model.transcribe(nombre_archivo)
        return(result["text"])