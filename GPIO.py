import  RPi.GPIO as GPIO
import time
from  camera import picture_save
from  text_to_speech import text_to_speech, play_wav 
from face import identify

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)

person_name = []
filename = "test.jpg"

while True:
    inputA = GPIO.input(18)
    inputB = GPIO.input(15)
    inputC = GPIO.input(23)

    if (inputA == False):
        print("Button A press ")
        picture_save(1, filename)
        person = identify(0, filename)
        print(person)
    if (inputB == False):
        print("Button B press ")
        response = "Is enemy..."
        filename = "response.wav"
        text_to_speech(response, filename)
        play_wav(filename)
    if (inputC == False):
        print("Button C press ")
    time.sleep(0.2)
