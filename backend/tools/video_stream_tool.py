
import cv2

def get_frame(stream_url):
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("❌ Cannot open stream")
        return None

    # 🔥 Read a few frames (important for MJPEG stability)
    for _ in range(5):
        ret, frame = cap.read()

    cap.release()

    if ret:
        return frame

    return None
