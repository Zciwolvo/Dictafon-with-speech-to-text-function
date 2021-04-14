#!/usr/bin/env python3
import speech_recognition as sr
import sounddevice as sd

audio = []  #if you want to get speech to text from previously prepared file write path to it here (replace [] with your "string")
r = sr.Recognizer()
#---------------------------------------------
if audio == []:
    fs=44100
    duration = 5
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')      #that thing records audio
    print ("Recording Audio")
    with sr.Microphone() as source:
        audio = r.listen(source)
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    sd.wait()
    print ("Audio recording complete")
#---------------------------------------------
else:
    with sr.AudioFile(audio) as source:
        audio = r.listen(source)

try:
    f = open("text.txt", "w+")
    f.write(r.recognize_google(audio, language="eng-ENG"))
    print("Your text file is ready")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")                   #that thing makes whole speech to text thing
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#---------------------------------------------

