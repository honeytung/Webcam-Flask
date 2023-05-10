import cv2

url = 'http://127.0.0.1:5000/video_feed'
cap = cv2.VideoCapture(url)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()