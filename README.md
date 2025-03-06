# 🎧 Speech-to-Text (STT) with Vosk

This project is a **Speech-to-Text (STT) system** that utilizes **Vosk** for offline speech recognition. It processes an audio file, converts it into the correct format, and then transcribes it into text.

## 🚀 Features

- ✅ **Offline Speech Recognition** using the **Vosk** API  
- 🎧 **Supports WAV audio files**  
- 📝 **Generates accurate transcriptions**  
- 🛆 **Lightweight and efficient**  

---

## 💂️ Project Structure

> **Note:** Before running the project, download, extract, and rename the **Vosk** model folders and place them in the project directory.

```
stt-vosk-py/
│── .gitignore                     # Git ignore file
│── main.py                         # Main script to process and transcribe audio
│── util.py                         # Utility functions for audio processing
│── requirements.txt                 # Dependencies for the project
│── README.md                        # Project documentation
│── harvard.wav                      # Example input audio file
│── sample.wav                       # Processed audio file
│── srt-3.5.3-py3-none-any.whl       # Wheel file for SRT
│── vosk-model/  # Pre-trained medium Vosk model (❗ Required)
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone <repository-url>
cd stt-vosk-py
```

### 2️⃣ Install Dependencies  

#### ✅ **Automatic Installation**
```sh
pip install -r requirements.txt
```

#### 🛠 **Manual Installation**
```sh
pip install pyaudio
```
```sh
pip install pydub
```
```sh
pip install srt-3.5.3-py3-none-any.whl
```
```sh
pip install vosk
```

### 3️⃣ Download & Set Up the Vosk Model  

1. Download the Vosk models from [Vosk Models](https://alphacephei.com/vosk/models).

 #### Example for English US models
![Example for English US models](./img/en-models.png)
2. Extract the model and rename it as:
   - `vosk-model`

3. Place it inside the **project directory**.

---

## 🚀 Usage

1. Replace `harvard.wav` with your input audio file in the project directory and update `AUDIO_INPUT` in `util.py` to match the file name.
2. Run the main script:  
   ```sh
   python main.py
   ```
   #### It will display `Do you want to transcribe audio live? (y/n): `
   #### Choose whether you want to transcribe live or not
3. The transcribed text will be **printed in the console**.  

---