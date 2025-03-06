import util

def main():
    ans = input("Do you want to transcribe audio live? (y/n): ")
    if ans.lower() == "y":
        util.transcribe_audio_live()
    else:
        util.transcribe_audio()

if __name__ == "__main__":
    main()