import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    check,frame=video.read()
    print(frame)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow('livecam',frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(faces)
video.release()
cv2.destroyAllWindows()