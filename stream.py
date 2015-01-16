import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

i = 0

while True:
    i=i+1
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    cv2.imwrite("stream/temp" + str(i) + ".jpg", frame, (cv2.IMWRITE_JPEG_QUALITY, 80))
    os.rename("stream/temp" + str(i) + ".jpg", "stream.jpg")

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
