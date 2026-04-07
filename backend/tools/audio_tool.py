import sounddevice as sd
import numpy as np

def record_audio(duration=3, fs=22050):
    print("🎤 Listening...")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    return audio.flatten(), fs
