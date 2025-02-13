import speech_recognition as sr
import os
import sys
import webbrowser
import pyaudio
import whisper
import numpy as np
import torch
import whisper
import librosa
from docx import Document
import subprocess
import aspose.words as aw



word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
# model = whisper.load_model('medium')
model = whisper.load_model("medium")
recognizer = sr.Recognizer()


def movement(command):
    if 'открой браузер' in command:
        webbrowser.open("https://www.google.com")
    elif "как дела" in command:
        print("У меня всё отлично, спасибо!")
    elif "cоздай документ" in command:
        doc = Document()
        doc.add_paragraph(command)
        doc.save("new.docx")
        print("Документ успешно создан!")

    elif "открой документ" in command:
        try:
            subprocess.Popen([word_path])
            print("Microsoft Word успешно запущен.")
        except FileNotFoundError:
            print("Не удалось найти Microsoft Word по указанному пути.")

def record():
    with sr.Microphone() as source:
        print('Скажите что-нибудь!')
        audio = recognizer.listen(source)
            # Сохранение аудио в файл
        with open("speech.wav", "wb") as f:
            f.write(audio.get_wav_data())

        try:
            audio, srate = librosa.load("speech.wav", sr=16000)
            result = model.transcribe(audio,language = "ru")
            text = result["text"].strip().lower()
            print(f"Вы сказали: {text}")


        except sr.UnknownValueError:
            print("Извините, я не смог распознать вашу речь.")  # Обработка ошибки распознавания  
        return text  


while True:
    command = record()

    movement(command=command)



