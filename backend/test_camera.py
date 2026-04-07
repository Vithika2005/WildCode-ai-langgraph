from tools.video_stream_tool import get_frame
from config import STREAM_URL
import cv2

frame = get_frame(STREAM_URL)

if frame is None:
    print("❌ No frame received")
else:
    print("✅ Frame received")
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
