import speech_recognition as sr
from pydub import AudioSegment

mp3_file_path = "../../mp3/test_gtts_de.mp3"
audio = AudioSegment.from_mp3(mp3_file_path)

recognizer = sr.Recognizer()

audio_data = sr.AudioData(audio.raw_data, audio.frame_rate, audio.sample_width)
try:
    text = recognizer.recognize_google(audio_data, language="de-DE")
    print("\nTranscription:\n", text, "\n")
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
