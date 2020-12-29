import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
#img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png")#to print the shape of the image
#print(img.shape) #shows height, width, pixel RGB
#imgresized=cv2.resize(img,(300,500))#to resize the image (give width, height)
#imgcropped=img[200:400,200:400] #to crop (height , width) of the image
#cv2.imshow("output",imgresized)

#img=np.zeros((512,512,3),np.uint8) #zeros refers to a black image, adding a 3 converts from grayscale to bgr image
#img[:]=255,0,0  #convert entire image to blue color
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #to make a green diagonal line from 0,0 to width,height point of thickness 3
#cv2.rectangle(img,(0,0),(300,400),(0,255,0),3) #to make a green rectangle from 0,0 to 300,400 point
#cv2.circle(img,(400,50),30,(0,0,150),3)  #to make a red circle of radius 30
#cv2.putText(img,"OpenCV",(300,200),cv2.FONT_ITALIC,1,(0,150,0),2) # to write green text
#cv2.imshow("output",img)

def empty(w):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,480)
cv2.createTrackbar("Hue Min","TrackBars",3,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",115,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
while True:
    img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png")
    imgresized = cv2.resize(img, (300, 500))
    imgHSV=cv2.cvtColor(imgresized,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgresult=cv2.bitwise_and(imgresized,imgresized,mask=mask)

    #cv2.imshow("output",imgHSV)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Result",imgresult)
    imgstack=stackImages(0.6,([imgresized,imgHSV],[mask,imgresult]))
    cv2.imshow("Stacked images",imgstack)

    cv2.waitKey(1)