import librosa
import numpy as np

def extract_features(audio, sr):
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)


def detect_roar(audio, sr):
    features = extract_features(audio, sr)

    energy = np.mean(np.abs(audio))

    # 🔥 Simple logic (baseline)
    if energy > 0.05:
        return "Loud sound detected"

    return "No roar detected"
