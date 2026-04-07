import time
from orchestration.pipeline import run_pipeline
from tools.firebase_tool import get_sensor_data

running = False

def start_realtime_loop(interval=3):
    global running
    running = True

    print("🚀 Real-time monitoring started...")

    last_data = None

    while running:
        data = get_sensor_data()

        if data != last_data:
            print("\n🔥 CHANGE DETECTED IN FIREBASE")

            result = run_pipeline()

            print("📊 RESULT:")
            print(result)

            last_data = data

        time.sleep(interval)


def stop_realtime_loop():
    global running
    running = False
    print("🛑 Real-time monitoring stopped")
