import os
import wave
import json
from vosk import Model, KaldiRecognizer
from util import convert_audio

MODEL_PATH = "vosk-model" # Medium model for general use
AUDIO_INPUT = "harvard.wav"
AUDIO_PROCESSED = "sample.wav"
SAMPLE_RATE = 16000

if not os.path.exists(MODEL_PATH):
    print(f"Model '{MODEL_PATH}' not found!")
else:
    print("Model found!")

if convert_audio(AUDIO_INPUT, AUDIO_PROCESSED):
    print("🔄 Converted audio ready!")

if not os.path.exists(AUDIO_PROCESSED):
    print(f"Audio file '{AUDIO_PROCESSED}' not found! Please provide a valid WAV file.")
    exit()
else:
    print("Audio file found!")

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
recognizer.SetWords(True)

with wave.open(AUDIO_PROCESSED, "rb") as wf:
    print(f"Channels: {wf.getnchannels()}")
    print(f"Sample Rate: {wf.getframerate()}")
    print(f"Sample Width: {wf.getsampwidth()} (2 = 16-bit PCM)")
print(f"Total frame samples: {wf.getnframes()}")

wf = wave.open(AUDIO_PROCESSED, "rb")
audio_data = wf.readframes(wf.getnframes())
wf.close()

print("Processing Audio File...")
print("Partial result:", recognizer.PartialResult())
print("Transcription complete!")