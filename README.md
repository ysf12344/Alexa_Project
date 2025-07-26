# Basic Alexa Project
Mini project based on Python
🎙️ Voice Assistant in Python (Arabic + YouTube Music Integration)

This project is a simple voice assistant built with Python that listens for Arabic voice commands, speaks responses using Google Text-to-Speech, and can play music from YouTube using the YouTube Data API and Selenium.
🚀 Features

    Speech Recognition (Arabic - Morocco locale) using Google Speech Recognition.

    Text-to-Speech output via gTTS (Google Text-to-Speech).

    Command Processing with basic natural language handling.

    Play YouTube Music based on voice commands using the YouTube Data API and Selenium.

    Arabic support: The assistant understands and responds in Arabic.

🎧 Sample Voice Commands
Command (Voice Input)	Action
"ما هو الوقت الآن؟"	Responds with the current time
"ما هو التاريخ الآن؟"	Tells today’s date
"ما اسمك؟"	Responds with assistant's name
"خدمي لينا الشعبي"	Opens YouTube and plays a Chaabi playlist
"Thank you"	Replies with a welcome message
🛠️ Technologies Used

    speech_recognition: For capturing and interpreting voice input

    gTTS + playsound: For speech output

    selenium + youtube-api-python-client: For searching and playing YouTube music

    datetime, requests, os, threading, random: Various utilities

📁 Project Structure

.
├── alexa_youssef.py          # Main voice assistant logic (speech-to-text, response handling)
├── Youtube_API.py   # YouTube music playback logic using Selenium and YouTube API

📌 Prerequisites

    Python 3.7+

    Chrome & ChromeDriver installed

    Google API key with access to YouTube Data API v3

🔐 Setup

    Install required packages:

pip install gTTS playsound selenium google-api-python-client speechrecognition

Add your YouTube API key in Youtube_API.py:

DEVELOPER_KEY = "YOUR_API_KEY_HERE"

Run the assistant:

    python alexa_youssef.py


