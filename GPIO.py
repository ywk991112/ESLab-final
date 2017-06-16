import  RPi.GPIO as GPIO
import time
from  camera import picture_save
from  text_to_speech import text_to_speech, play_wav 
from face import identify
from db import db
from audio_transcribe import audio_transcribe, record_sound

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)

person = "chou"
result = ""

while True:
    inputA = GPIO.input(18)
    inputB = GPIO.input(15)
    inputC = GPIO.input(23)

    if (inputA == False):
        print("Button A press ")
        filename = "test.jpg"
        picture_save(1, filename)
        person = identify(0, filename)
        print(person)
    if (inputB == False):
        print("Button B press ")
        response = "Is enemy..."
        if (db[person]["is_enemy"]):
            response = "Is enemy ..."
        else:
            response = "not enemy ..."
        filename = "response.wav"
        text_to_speech(response, filename)
        play_wav(filename)
    if (inputC == False):
        print("Button C press ")
        file_name = "sound.wav"
        if (record_sound(file_name) ):
            print("Record success!")
        result = audio_transcribe(file_name)
        print(result) 
        response = "Please, say again sir .."
        if("enemy" in result):
            if (db[person]["is_enemy"]):
                response = person + " is enemy, sir ..."
            else:
                response = person + " is not enemy, sir  ..."
        elif("weakness" in result):
            response = "hit " + person + " in " + db[person]["weakness"] + " sir  ..."
        filename = "response.wav"
        text_to_speech(response, filename)
        play_wav(filename)

    time.sleep(0.2)
