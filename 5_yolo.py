from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

cap.set(4, 640) #cap.set(3, 640)
cap.set(3, 480) #cap.set(4, 480)wц

while True:
    _, img = cap.read()

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img)
    for r in results:
        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            if model.names[int(box.cls)] != "person": continue
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            (top, left, bottom, right) = b.numpy().astype(int)
            img[left:right, top:bottom, 0] = 255
            annotator.box_label(b, model.names[int(c)])

    img = annotator.result()
        
    cv2.imshow('YOLO V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllцWindows()