#!/usr/bin/env python3

import speech_recognition as sr
import sys
import os

# obtain path to "english.wav" in the same folder as this script
from os import path
# file_name = sys.argv[1]
path_file = "audio/"

def record_sound(file_name):
    os.system("arecord --format=S16_LE --duration=3 --rate=16k " + path_file + str(file_name) + " -D sysdefault:CARD=1" )
    return True


def audio_transcribe(file_name):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), path_file + file_name)
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    result = ""

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        result = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return result

if __name__ == '__main__':
    file_name = "a.wav"
    record_sound(file_name)
    result = audio_transcribe(file_name)
    print(result) 
