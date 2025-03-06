# Speech-to-Text (STT) with Vosk

This project is a **Speech-to-Text (STT) system** using **Vosk** for offline speech recognition. It processes an audio file, converts it into the correct format, and then transcribes it into text.

## 🚀 Features

- Uses **Vosk** for offline speech recognition
- Supports transcription of **WAV audio files**

## 📂 Project Structure

### you need to download, extract, and rename the **Vosk** model folders and add them to the project

```
stt-vosk-py/
|__ .gitignore         # Git ignore file
│── main.py            # Main script to process and transcribe audio
│── util.py            # Utility functions for audio processing
│── requirements.txt   # Dependencies for the project
│── README.md          # Project documentation
│─x vosk-model-en-us-medium-lgraph/ # Pre-trained medium Vosk model
│─x vosk-model-en-us-small/ # Pre-trained small Vosk model
│── harvard.wav        # Example input audio file
│── sample.wav         # Processed audio file
│── srt-3.5.3-py3-none-any.whl # Wheel file for srt
```

## 🛠️ Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd stt-vosk-py
    ```
2. Install Libraries

    2.1. Automatic Installation

    ```sh
    pip install -r requirements.txt
    ```
    2.2. Manual Installation

    ```sh
    pip install pydub
    pip install srt-3.5.3-py3-none-any.whl
    pip install vosk
    ```

4. Download and extract the Vosk model:
    - Place the extracted model in the project directory.

## 🚀 Usage

1. Ensure your input audio file (`harvard.wav`) is in the project directory.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The transcribed text will be printed in the console.