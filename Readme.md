# Recognition Helmet
This is the final project of Embedded System course in NTUEE.

![alt text](https://github.com/ywk991112/ESLab-final/blob/master/picture/result.jpg)
- [Report](https://github.com/ywk991112/ESLab-final/blob/master/Report.pdf)
- [Video](https://www.youtube.com/watch?v=40-1K9EXpRs&feature=youtu.be)

## Files description

### GPIO.py
```
python3 GPIO.py
```
The main file of the whole project. While executing, the three modules start listening to the input.

### face.py
Functions of face recoginition is written in this file.

### camera.py
Functions of R pi camera module

### text_to_speech.py
Functions of reading text and output an audio file.

### audio_transcribe.py
Functions of reading audio file and transcribing into text.

### db.py
Database for the information.

### ref/
Some other reference files.

## Run the code on Raspberry pi 3
We use R pi3 and Ubuntu 16.04 mate.
Please refer to 'Report.pdf' if you want to implement yourself...

### R pi software installation
```

// setup
sudo pip3 install ipython
sudo apt-get update
sudo apt-get upgrade

// speech recognition 
sudo pip3 install SpeechRecognition
sudo apt-get install portaudio19-dev
sudo pip3 install PyAudio


// Test usb microphone
// record -- bad quality... but can work
arecord a.wav -D sysdefault:CARD=1
arecord --format=S16_LE --duration=5 --rate=16k a.wav -D sysdefault:CARD=1
// playback
 omxplayer -p -o local a.wav
// Test to speech
sudo pip3 install gTTS


// GPIO
sudo pip3 install GPIO // then use the example

// cognitive face
sudo pip3 install cognitive_face

```

