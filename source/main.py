import cv2
import pickle
import cvzone
import numpy as np
from shapely.geometry import Point, Polygon

cap = cv2.VideoCapture('source\Ressources\webcam.mp4')
with open('source\Ressources\CarParkPos', 'rb') as f:
    posList = pickle.load(f)


def empty(a):
    pass


cv2.namedWindow("Vals")
cv2.resizeWindow("Vals", 640, 240)
cv2.createTrackbar("Val1", "Vals", 25, 50, empty)
cv2.setTrackbarMin("Val1", "Vals", 10)
cv2.createTrackbar("Val2", "Vals", 16, 50, empty)
cv2.setTrackbarMin("Val2", "Vals", 1)
cv2.createTrackbar("Val3", "Vals", 5, 50, empty)
cv2.setTrackbarMin("Val3", "Vals", 1)


def checkSpaces():
    spaces = 0
    for pos in posList:

        mask = np.zeros((imgThres.shape[0], imgThres.shape[1]), dtype=np.uint8)
        cv2.fillPoly(mask, [pos], 255)
        masked = cv2.bitwise_and(imgThres, imgThres, mask=mask)
        count = cv2.countNonZero(masked)

        if count < 1000:
            color = (0, 200, 0)
            thic = 5
            spaces += 1

        else:
            color = (0, 0, 200)
            thic = 2
        
        cv2.polylines(img, [pos], True, color, thic)
        
        #Sort points so the most upper left is in first position
        points = np.squeeze(pos)
        rect = np.zeros((4, 2), dtype = "float32")
        s = points.sum(axis = 1)
        rect[0] = points[np.argmin(s)]
        rect[2] = points[np.argmax(s)]
        diff = np.diff(points, axis = 1)
        rect[1] = points[np.argmin(diff)]
        rect[3] = points[np.argmax(diff)]

        x,y = rect[0]
        
        cv2.putText(img, str(count), (int(x) + 6, int(y) + 15), cv2.FONT_HERSHEY_PLAIN, 1, color, 2)

    cvzone.putTextRect(img, f'Frei: {spaces}/{len(posList)}', (50, 60), thickness=3, offset=20, colorR=(0, 200, 0))


while True:

    # Get image frame
    success, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    # img = cv2.imread('img.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    # ret, imgThres = cv2.threshold(imgBlur, 150, 255, cv2.THRESH_BINARY)

    val1 = cv2.getTrackbarPos("Val1", "Vals")
    val2 = cv2.getTrackbarPos("Val2", "Vals")
    val3 = cv2.getTrackbarPos("Val3", "Vals")
    if val1 % 2 == 0: val1 += 1
    if val3 % 2 == 0: val3 += 1
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, val1, val2)
    imgThres = cv2.medianBlur(imgThres, val3)
    kernel = np.ones((3, 3), np.uint8)
    imgThres = cv2.dilate(imgThres, kernel, iterations=1)

    checkSpaces()
    # Display Output

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Image", img)
    #cv2.imshow("ImageGray", imgThres)
    #cv2.imshow("ImageBlur", imgBlur)
    pressedKey = cv2.waitKey(1)
    if pressedKey == 27: # escape key
        break