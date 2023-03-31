import cv2
import pickle

width, height = 107, 48
parkPosData = 'source\Ressources\CarParkPos'
parkPosImage = 'source\Ressources\parkPositions.png'

try:
    with open(parkPosData, 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open(parkPosData, 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread(parkPosImage)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.namedWindow("ParkingPositionPlacer", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("ParkingPositionPlacer", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("ParkingPositionPlacer", img)

    cv2.setMouseCallback("ParkingPositionPlacer", mouseClick)
    pressedKey = cv2.waitKey(1)
    if pressedKey == 27: # escape key
        break