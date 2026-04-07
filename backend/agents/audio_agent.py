
from tools.audio_tool import record_audio
from ml.audio_model import detect_roar

def audio_agent():

    audio, sr = record_audio()

    result = detect_roar(audio, sr)

    if "Loud" in result:
        return {"audio": "⚠️ Possible roar or loud disturbance detected"}

    return {"audio": "No roar detected"}
