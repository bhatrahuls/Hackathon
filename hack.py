'''import cv2,time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
address= "http://100.66.185.24:8080/video"
video.open(address)
while True:
	check,frame=video.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face=face_cascade.detectMultiScale(gray, 
    scaleFactor=1.1, 
    minNeighbors=5)
	for x,y,w,h in face:
		img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
	cv2.imshow("g",frame)
	key=cv2.waitKey(1)
	
	if key==ord('q'):
		break
video.release()
cv2.destroyAllWindows'''
import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
address= "http://192.168.209.29:8080/video"
cap.open(address)
while True:
    _, img =cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()