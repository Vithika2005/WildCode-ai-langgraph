from tools.video_stream_tool import get_frame
from ml.video_model import detect_objects
from config import STREAM_URL

def fencing_agent(data):
    motion = data.get("motion", 0)

    # 🔒 Step 1: No motion → skip expensive vision
    if not bool(motion):
        return {"fence": "No motion"}

    print("📸 Motion detected → capturing frame")

    frame = get_frame(STREAM_URL)

    if frame is None:
        return {"fence": "Motion detected but no video"}

    objects = detect_objects(frame)

    print("🧠 YOLO detected:", objects)

    # 🔥 Step 2: Smart decisions
    if "person" in objects:
        return {"fence": "🚨 HUMAN DETECTED NEAR FENCE"}

    wildlife = ["dog", "cow", "horse", "elephant", "bear"]

    for animal in wildlife:
        if animal in objects:
            return {"fence": f"🐾 Animal detected: {animal}"}

    return {"fence": "Motion detected but unknown object"}
