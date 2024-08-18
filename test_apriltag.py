from pupil_apriltags import Detector
import cv2


at_detector = Detector(
   families="tag36h11",
)

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = at_detector.detect(frame)
    print(res)
    cv2.imshow('Apriltag', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()