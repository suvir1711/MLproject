import cv2  # for capturing videos
import math  # for mathematical operations
import os

import pandas as pd

count = 0
videoFile = "test_video/liveMrdr.mp4"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5)  # frame rate
x = 1
while cap.isOpened():
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()
    if ret != True:
        break
    if frameId % math.floor(frameRate) == 0:
        filename = "test_image/harm/test%d.jpg" % count;
        count += 1
        cv2.imwrite(filename, frame)
cap.release()
print("Done!")

path = 'test_image/harm'

files = []

for f in os.listdir(path):
    files.append(f)
# print files

b = ["Image_ID"]
s = pd.DataFrame(files, columns=b)
s = s.sort_values('Image_ID', ascending=True)
s.to_csv('test.csv', index=False)
print("done")
