# Personal virtual Assistant **`POGO`**

Pogo is a Python-based personal virtual assistant that allows you to control your computer using voice commands. It is designed to assist you with various tasks using natural language interactions.

## Overview

Pogo is an intelligent virtual assistant programmed to understand and execute a variety of commands to help you with daily tasks. It utilizes speech recognition and text-to-speech synthesis to interact with users. Whether you want to open applications, check the weather, listen to the news, play music, or search the web, Pogo is here to assist you!

## Features

### 1. Wake Word Detection
- **Wake Word**: Listens for the wake word "Pogo" to activate the assistant.

### 2. Open Applications
- **Open Notepad**: Launches the Notepad application.
- **Open Calculator**: Opens the Calculator application.
- **Open Paint**: Launches Microsoft Paint.
- **Open File Explorer**: Opens the File Explorer.

### 3. Browse Websites
- **Open Google**: Opens Google in your default web browser.
- **Open Facebook**: Opens Facebook in the browser.
- **Open YouTube**: Opens YouTube in the browser.
- **Open LinkedIn**: Opens LinkedIn in the browser.
- **Open GitHub**: Opens GitHub in the browser.
- **Open Twitter**: Opens Twitter in the browser.
- **Open ChatGPT**: Opens ChatGPT website for AI.

### 4. Play Music
- **Play Music**: Plays music by searching for the song in a predefined music library(You can create your own library by editing the musicLibrary.py file).

### 5. Get News Headlines
- **News**: Fetches and speaks the latest news headlines from various sources. 

### 6. Check Weather
- **Weather in [City]**: Retrieves and speaks the current weather for the specified city.

### 7. Google Search
- **Search [Query]**: Performs a Google search based on the user's query.

### 8. Stop Command
- **Stop**: Stops the assistant and exits.

## Voice Assistant Demo

Watch the demo video of my personal voice assistant:
<br>click here
<br>👇👇👇

[![Voice Assistant Demo](https://img.youtube.com/vi/lgVoEzpXrAA/0.jpg)](https://www.youtube.com/watch?v=lgVoEzpXrAA)




## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kindo-tk/virtual_assistant.git
   ```
2. **Navigate to the project directory:**

    ```sh
    cd .\virtual_assistant\
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

4. **Activate the virtual environment:**

   ```sh
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the assistant:

   ```bash
   python main.py
   ```

2. Wait for the wake word "Pogo" to activate the assistant.
3. Give voice commands to perform various tasks.
4. To exit give stop as command.

## Note

1. **API Keys:**
   - Please use your own API keys for the news and weather APIs. Replace the placeholders in the code with your own API keys to access these services.

2. **Speech Recognition:**
   - Sometimes the assistant may have difficulty recognizing speech accurately. If you encounter recognition issues, try speaking clearly and ensure there is minimal background noise. Additionally, you can adjust the microphone settings for better recognition.

3. I have added an executable file <a href ="https://github.com/kindo-tk/voice_assistant/blob/main/Pogo.exe">`pogo.exe`</a> that allows you to use the voice assistant directly without any installation process.(your antivirus may show this as a threat, but it is completely safe).

## Area of Improvement:

One area for potential improvement is the integration of OpenAI into Pogo. Incorporating OpenAI would enhance Pogo's capabilities, making it a true AI assistant with advanced natural language understanding and more powerful features. However, this is currently limited by the paid nature of the APIs.

## Contributing

Contributions to improve Pogo are welcome! If you have any bug fixes, feature requests, or enhancements, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact 
For any inquiries or feedback, please contact:

- <a href="https://www.linkedin.com/in/tufan-kundu-577945221/">Tufan Kundu (LinkedIn)</a>
- Email: tufan.kundu11@gmail.com
