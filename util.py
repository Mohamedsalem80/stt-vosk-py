import os
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

MODEL_PATH = "vosk-model"
AUDIO_INPUT = "harvard.wav"
AUDIO_PROCESSED = "sample.wav"
SAMPLE_RATE = 16000
CHUNK_SIZE = 4000

def convert_audio(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_sample_width(2)
        audio.export(output_path, format="wav")
        print(f"Conversion successful: {output_path}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
    

def transcribe_audio_live():
    if not os.path.exists(MODEL_PATH):
        print(f"Model '{MODEL_PATH}' not found!")
        return

    print("Model found! Loading...")
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)
    recognizer.SetWords(True)

    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
    )
    stream.start_stream()

    print("Listening... (Press Ctrl+C to stop)")
    try:
        while True:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

            # Process partial words instantly
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print(result['text'])
            else:
                partial_result = json.loads(recognizer.PartialResult())
                if "partial" in partial_result:
                    print(partial_result['partial'], end="\r")  # Show words in real-time

    except KeyboardInterrupt:
        print("\nStopping transcription...")
        stream.stop_stream()
        stream.close()
        p.terminate()

def transcribe_audio():
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
    if recognizer.AcceptWaveform(audio_data):
        result = json.loads(recognizer.Result())
        print("Transcription:", result['text'])
    else:
        print("Error in transcription!")
    wf.close()

    print("Processing Audio File...")
    print("Partial result:", recognizer.PartialResult())
    print("Transcription complete!")
