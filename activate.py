import speech_recognition as sr
import os
import sys
import webbrowser
import pyaudio
import whisper
import numpy as np
import torch
from vosk import Model,KaldiRecognizer

# model = whisper.load_model('medium')
model = Model("vosk-model-en-us-0.22")
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Скажите что-нибудь!')
    audio = recognizer.listen(source)
    audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
    audio_data = audio_data.astype(np.float32) / 32768.0 # нормализация до [-1 1]
    
    try:
        text = model.transcribe(audio_data)
        result = text["text"].strip().lower()
        print(f"Вы сказали: {result}")

    
        if 'открой браузер' in text:
            webbrowser.open("https://www.google.com")
        elif "как дела" in text:
            print("У меня всё отлично, спасибо!") 
            
    except sr.UnknownValueError:
        print("Извините, я не смог распознать вашу речь.")  # Обработка ошибки распознавания
