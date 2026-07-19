from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8s.pt")

def detect_objects(frame):
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.5,
        verbose=False,
    )
    annotated_frame = results[0].plot()
    return annotated_frame