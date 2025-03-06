from pydub import AudioSegment

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