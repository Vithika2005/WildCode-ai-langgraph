
from flask import Flask, jsonify
from flasgger import Swagger
import threading

# 🔌 Pipeline + Realtime
from orchestration.pipeline import run_pipeline
from orchestration.realtime_runner import (
    start_realtime_loop,
    stop_realtime_loop
)
app = Flask(__name__)
swagger = Swagger(app)

# 🏠 Home
@app.route("/")
def home():
    return {"message": "Aaranyak-AI running"}


# 🚀 Run full pipeline (manual trigger)
@app.route("/run", methods=["GET"])
def run():
    """
    Run Aaranyak AI pipeline
    ---
    responses:
      200:
        description: Pipeline output
    """
    result = run_pipeline()
    return jsonify(result)


# ⚡ Start real-time monitoring (background thread)
@app.route("/start-realtime", methods=["GET"])
def start_realtime():
    """
    Start real-time Firebase monitoring
    ---
    responses:
      200:
        description: Realtime started
    """

    thread = threading.Thread(target=start_realtime_loop)
    thread.daemon = True  # 🔥 ensures it stops with Flask
    thread.start()

    return {"message": "Real-time monitoring started"}
@app.route("/stop-realtime", methods=["GET"])
def stop_realtime():
    """
    Stop real-time monitoring
    ---
    responses:
      200:
        description: Realtime stopped
    """
    stop_realtime_loop()
    return {"message": "Real-time monitoring stopped"}

# ▶️ Run server
if __name__ == "__main__":
    app.run(debug=True)
