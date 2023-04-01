import cv2
import pickle
import numpy
from shapely.geometry import Point, Polygon
import easygui

parkPosData = "source\data\\" + easygui.enterbox("What parking slot file do you want to create/edit?")
parkPosImage = easygui.fileopenbox(title="Select example image...", filetypes=[["*.png", "*.jpg", "*.jpeg", "Images"]])

if not parkPosData or not parkPosImage:
    exit()

# parkPosData = 'source\data\CarParkPos'
# parkPosImage = 'source\media\parkPositions.png'

tempCoords = []

try:
    with open(parkPosData, 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        tempCoords.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            polygon = Polygon(numpy.squeeze(pos))
            point = Point(x,y)
            if polygon.contains(point):
                posList.pop(i)

    with open(parkPosData, 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread(parkPosImage)
    if len(tempCoords) > 0:
        for p in tempCoords:
            cv2.circle(img, p, 0, (255, 0, 255), 5)

    if len(tempCoords) > 1:
        for x in range(len(tempCoords)):
            cv2.line(img, tempCoords[x-1], tempCoords[x], (255, 0, 255), 2)

    if len(tempCoords) > 3:
        pts = numpy.asarray(tempCoords, numpy.int32)
        pts = pts.reshape((-1,1,2))
        posList.append(pts)
        tempCoords = []

    for pos in posList:
        cv2.polylines(img, [pos], True, (255, 0, 255), 2)

    cv2.namedWindow("ParkingSpacePicker", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("ParkingSpacePicker", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("ParkingSpacePicker", img)

    cv2.setMouseCallback("ParkingSpacePicker", mouseClick)
    pressedKey = cv2.waitKey(1)
    if pressedKey == 27: # escape key
        break