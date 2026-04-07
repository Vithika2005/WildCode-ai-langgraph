from ultralytics import YOLO

# Load once (important)
model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)

    detected = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detected.append(label)

    return detected
