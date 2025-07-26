# Import the required libraries
import webbrowser  # Used to open web pages in the browser
from Youtube_API import play
from time import ctime
from time import sleep
import time  # Used to get the current time
from datetime import datetime
import requests
from datetime import date
import os  # Used for interacting with the operating system (like deleting files)
import playsound  # Used to play sound files
from gtts import gTTS  # Google Text-to-Speech for converting text to speech
import random  # Used to perform random operations (not used in this code yet)
import speech_recognition as sr  # Library to recognize speech input from the microphone
# from project import open_browzer
import threading  # Used to run background tasks (not used in this code yet)

# Define the voice assistant class
class voice_assistant:
    # Create a single recognizer instance from speech_recognition library
    recognizer = sr.Recognizer()

    # Method to record audio from the microphone
    def record_audio(self):
        with sr.Microphone() as source:  # Open the default microphone as an audio source
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            audio = self.recognizer.listen(source)  # Listen and capture the audio
        return audio  # Return the recorded audio

    # Method to convert recorded audio into text
    def recognize_speech(self, audio):
        try:
            # Use Google's speech recognition for Arabic (Egypt) to convert speech to text
            text = self.recognizer.recognize_google(audio, language="ar-MA")
            # Alternative engine (commented out): Whisper
            # text = self.recognizer.recognize_whisper(audio, language="arabic")
            print(f"You said: {text}")
            return text  # Return the recognized text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")  # Handle case when speech is not recognized
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")  # Handle connection or request error
        return ""  # Return empty string on error

    # Method to convert text to speech and play it
    def speak(self, audios):
        tts = gTTS(text=audios, lang='ar', slow=False)  # Convert text to Arabic speech
        audioF = 'audio.mp3'  # Define temporary filename for audio
        tts.save(audioF)  # Save the generated audio to a file
        playsound.playsound(audioF)  # Play the audio file
        print(audios)  # Also print the spoken text to the console
        os.remove(audioF)  # Delete the temporary audio file after playback


# Function to check if any word from a list exists in a given string
def search_words_in_string(word_list, text):
    # Check each word in word_list to see if it appears in the input text
    found_words = [word for word in word_list if word in text]
    return len(found_words) != 0, found_words  # Return True if at least one word is found, otherwise False

# Function to handle responses based on user voice input
def Respond(voice_data):
   
    
    global alexa
    a=voice_data.split()
    print(a)
    atime=["what","is","the","time","now"]
    nhar =["what","is","the","date","now"]
    brower= ["thank","you"]
    alex= ["what","name"]
    music=["play","music"]
    chaabi=["خدمي","لينا","الشعبي"]    
    

    if atime[0] and atime[3] in a:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        alexa.speak(current_time)
    elif nhar[0] and nhar[3] in a:
        today=date.today()

        
        alexa.speak(f"Today's date is {today.strftime('%B %d, %Y')}")    
   

    elif alex[0] and alex[1] in a:
        alexa.speak('my name is Alex')
    elif chaabi[0] and chaabi[1] and chaabi[2] in a:
        alexa.speak('حاضر هيا لولا')
        play('chaabi')
        # ه
    else: alexa.speak('مفهمتكش  ')
    

def alexa_actions():

    global alexa
    # lien="https://www.google.com/"

    # request=requests.get(lien)
    # file=request.content
    alexa.speak('you are welcome')
    return None




# Create an instance of the voice assistant
alexa = voice_assistant()

# Speak a greeting in Arabic
alexa.speak('salam a achiri')  # Good morning

# Keep the assistant running in a loop to continuously listen for input
while True:
    audio = alexa.record_audio()  # Record user input from the microphone
    voice_data = alexa.recognize_speech(audio)  # Convert the speech to text
    print(voice_data.lower())  # Print the recognized text in lowercase
    # Respond(str(voice_data))
    
    Respond(voice_data)
