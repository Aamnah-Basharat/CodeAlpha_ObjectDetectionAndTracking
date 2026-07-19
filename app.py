from flask import Flask, render_template, Response
from detector import detect_objects
import cv2

app = Flask(__name__)
camera = None

def generate_frames():
    global camera
    while True:
        if camera is None:
            break
        success, frame = camera.read()
        if not success:
            break
        frame = detect_objects(frame)
        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame
            + b"\r\n"
        )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_camera")
def start_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)
    return "Camera Started"

@app.route("/stop_camera")
def stop_camera():
    global camera
    if camera is not None:
        camera.release()
        camera = None
    return "Camera Stopped"

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )

if __name__ == "__main__":
    app.run(debug=True)