from gtts import gTTS
# from playsound import playsound
import pygame
import os

def text_to_speech(response, filename):

    #input_var = input("Enter something: ")
    print ("you entered " + response) 
    # response = intent_parser(input_var)
    print(response)


    tts = gTTS(text=response, lang='en', slow=True)

    #pygame.mixer.init()

    tts.save(filename)
    # playsound('hello.wav')
    #pygame.mixer.music.load("hello.wav")
    #pygame.mixer.music.play()
    # playsound('hello.mp3')

    
def play_wav(filename):
    print("Play music: ", filename)
    os.system("omxplayer -p -o local " + str(filename))
