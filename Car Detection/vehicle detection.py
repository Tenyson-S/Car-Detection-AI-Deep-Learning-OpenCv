import cv2
import imutils

cars_data='cars.xml'
car_cascade=cv2.CascadeClassifier(cars_data)

cam=cv2.VideoCapture('cars.mp4')

while True:
    _,frame=cam.read()
    frame=imutils.resize(frame,width=1000)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=car_cascade.detectMultiScale(gray,1.1,1)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("Frame",frame)

    b=str(len(cars))
    a=int(b)
    n=a
    print("-------------------------------------------------")
    print("North :%d:"%(n))
    if n>=8:
        print("North More traffic , please on the RED signal")
    else:
        print("No Traffic")

    if cv2.waitKey(33)==27:
        break

cam.release()
cv2.destroyAllWindows()
        
