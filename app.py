import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
import musicLibrary
import requests
import pygame
import tempfile
from googlesearch import search

# Initialize pygame mixer
pygame.mixer.init()

newsapi = "af4397d2094a4ec9bb22cc028beb84e1"
weather_api_key = "2e18e4ef351fba6f290c44d99284aa3c&units=metric"

def speak(text):
    """Converts text to speech using gTTS and plays the audio"""
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_filename = temp_file.name
            tts.save(temp_filename)  # Save the audio
        pygame.mixer.music.load(temp_filename)  # Load the audio after saving
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the audio finishes playing
            pygame.time.Clock().tick(10)  # Check every 10 milliseconds
        os.remove(temp_filename)  # Remove the temporary file after playing
    except Exception as e:
        print(f"Error in speak function: {e}")

def open_application(app_name):
    """Opens the specified application."""
    app_mapping = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "file": "explorer.exe"
    }
    if app_name in app_mapping:
        os.system(app_mapping[app_name])
        speak(f"{app_name.capitalize()} is now opened.")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

def get_news():
    """Fetches and speaks the latest news headlines"""
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        r.raise_for_status()  # Raise an exception for HTTP errors
        data = r.json()
        articles = data.get('articles', [])
        for article in articles[:5]:
            speak(article['title'])
    except Exception as e:
        speak(f"An error occurred while fetching news: {e}")

def get_weather(city):
    """Fetches and speaks the weather for a specified city"""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = r.json()
        temperature = weather_data["main"]["temp"]
        speak(f"The current temperature in {city} is {temperature} degrees Celsius.")
    except Exception as e:
        speak(f"An error occurred while fetching weather: {e}")

def search_google(query):
    """Performs a Google search and opens the first result"""
    try:
        search_results = list(search(query, num=1, stop=1))
        if search_results:
            webbrowser.open(search_results[0])
            speak(f"I have opened the page in your browser.")
        else:
            speak("I'm sorry, I couldn't find any results for your query.")
    except Exception as e:
        speak(f"An error occurred during the search: {e}")

def process_command(command):
    """Processes the given command and performs the appropriate action"""
    try:
        command = command.lower()

        if "open google" in command:
            webbrowser.open("https://google.com")
            speak("I have opened Google in your browser.")
        elif "open facebook" in command:
            webbrowser.open("https://facebook.com")
            speak("I have opened Facebook in your browser.")
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("I have opened YouTube in your browser.")
        elif "open linkedin" in command:
            webbrowser.open("https://linkedin.com")
            speak("I have opened LinkedIn in your browser.")
        elif "open github" in command:
            webbrowser.open("https://github.com/")
            speak("I have opened GitHub in your browser.")
        elif "open twitter" in command:
            webbrowser.open("https://x.com/")
            speak("I have opened Twitter in your browser.")
        elif "open chat" in command:
            webbrowser.open("https://chatgpt.com/")
            speak("I have opened ChatGPT in your browser.")
        elif command.startswith("play"):
            song = command.split("play", 1)[1].strip()
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
                speak(f"Song {song} is ready to be played.")
            else:
                speak("Sorry, I couldn't find the song in your music library.")
        elif "news" in command:
            get_news()
        elif "weather in" in command:
            city = command.split("weather in", 1)[1].strip()
            get_weather(city)
        elif "open" in command:
            app_name = command.split("open", 1)[1].strip()
            open_application(app_name)
        else:
            search_google(command)
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

# Main loop to keep listening for commands
if __name__ == "__main__":
    speak("Initializing Pogo...")
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000
    recognizer.dynamic_energy_threshold = True

    def listen_for_wake_word():
        """Listens for the wake word 'Pogo'"""
        while True:
            try:
                print("Listening for wake word...")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
                    audio = recognizer.listen(source, timeout=3)
                try:
                    word = recognizer.recognize_google(audio)
                    if "pogo" in word.lower():
                        speak("How may I help you?")
                        return
                except sr.UnknownValueError:
                    continue
                except sr.RequestError as e:
                    speak(f"Could not request results from Google Speech Recognition service; {str(e)}")
                except Exception as e:
                    speak(f"An unexpected error occurred: {str(e)}")
            except sr.WaitTimeoutError:
                continue
            except Exception as e:
                speak(f"An unexpected error occurred: {str(e)}")

    while True:
        listen_for_wake_word()
        try:
            print("Pogo Active, listening for command...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)

                if "stop" in command.lower():
                    speak("Signing off. Goodbye!")
                    break
                
                process_command(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {str(e)}")
        except Exception as e:
            speak(f"An unexpected error occurred: {str(e)}")
