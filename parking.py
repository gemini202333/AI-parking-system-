import cv2
import numpy as np
from object_detection import ObjectDetection
# Initialize Object Detection
od = ObjectDetection()
cap = cv2.VideoCapture("psauparkingvid.mp4")

while True:

    _, frame = cap.read()
    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        print(box)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
