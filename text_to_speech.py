from gtts import gTTS
from playsound import playsound

input_var = input("Enter something: ")
print ("you entered " + input_var) 
# response = intent_parser(input_var)
response = input_var
print(response)


tts = gTTS(text=response, lang='en', slow=True)


tts.save("hello.mp3")
playsound('hello.mp3')