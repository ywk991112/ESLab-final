from gtts import gTTS
# from playsound import playsound
import pygame

input_var = input("Enter something: ")
print ("you entered " + input_var) 
# response = intent_parser(input_var)
response = input_var
print(response)


tts = gTTS(text=response, lang='en', slow=True)

pygame.mixer.init()

tts.save("hello.wav")
# playsound('hello.wav')
pygame.mixer.music.load("hello.wav")
pygame.mixer.music.play()
# playsound('hello.mp3')
