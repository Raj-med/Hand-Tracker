
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    ret, img = cap.read()
    if not ret:
        break
    
    hands, img = detector.findHands(img, draw=True)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)
    
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
