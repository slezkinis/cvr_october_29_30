import cv2


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    lendth = (height // 100) * 52
    x_center = width // 2
    y_center = height // 2
    frame[y_center - (lendth // 2): y_center + (lendth // 2), x_center - (lendth // 2): x_center + (lendth // 2), 1:3] = (50, 200)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()