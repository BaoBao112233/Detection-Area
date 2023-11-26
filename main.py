import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

video = VideoStream(src=0).start()
# chúa các điểu để vẽ polygon
points = []

# model Yolo
model = YoloDetect()

# Reading image from Camera
# while True:
#     frame = video.read()

#     cv2.imshow("intrusion warning:",frame)
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x,y])

def draw_polygon(frame, points):
    for point in points:
        # vẽ điêm tròn màu đỏ BGR: (Blue, Green, Red)
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0,0,255), -1) 
    
    # vẽ đường nối các điểm lại với nhau bằng đường màu xanh dương
    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0,0), thickness = 2)
    return frame

detect = False

while True:
    frame = video.read()

    # Vẽ đa giác - polygon
    frame = draw_polygon(frame, points)


    if detect:
        frame = model.detect(frame, points)

    # Show ra màn hình 
    cv2.imshow("intrusion warning:",frame)

    # bắt sự kiện trên bàn phím
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord('d'):
        points.append(points[0])
        detect = True

    # bắt sự kiện chuột
    key = cv2.setMouseCallback('intrusion warning:', handle_left_click, points)

video.stop()
cv2.destroyAllWindow