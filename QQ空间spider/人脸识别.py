from cvs import *
import facerecognition
import numpy as np
from time import sleep
import time

camid = 1
cap = cvs.VideoCapture(camid)
facerecog = facerecognition.FaceRecognition("./models", 0.63)

fcount = 0
start = time.time()

while True:
    sleep(30)
    img = cvs.read()

    if img is None:
        continue

    fcount = fcount + 1
    # global lbs
    lbs = 'Average FPS: ' + str(fcount / (time.time() - start))
    cvs.setLbs(lbs)

    if camid == 1:
        img = cv2.flip(img, 1)

    # img=cv2.resize(img,(112,112))
    # image_char = img.astype(np.uint8).tostring()
    rets = facerecog.getfacepose(img.shape[0], img.shape[1], img)

    # print 'rets:',rets
    for ret in rets:
        # for ret in each:
        print('draw bounding box for the face')
        # cvs.infoshow('draw bounding box for the face')
        rect = ret['rect']
        # print rect
        mtcnn = ret['mtcnn']
        # print mtcnn
        for i in range(5):
            cvs.circle(img, (mtcnn[i], mtcnn[5 + i]), 2, (0, 0, 255), 2)
        keypoint = ret['keypoints']
        # print keypoint
        p1 = (int(rect[0]), int(rect[1]))
        p2 = (int(rect[0] + rect[2]), int(rect[1] + rect[3]))

        # draw_name(img, rect, ret['name'])
        cvs.rectangle(img, p1, p2, (0, 255, 0), 3, 1)
        for p in range(0, 106):
            k1 = int(rect[0] + keypoint[p * 2])
            k2 = int(rect[1] + keypoint[p * 2 + 1])
            cv2.circle(img, (k1, k2), 2, (253, 0, 0), 2)

    cvs.imshow(img)






