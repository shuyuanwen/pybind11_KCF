import cv2
import numpy as np
import matplotlib.pyplot as plt
import kcf_demo as kcf
import time


cv2.useOptimized()
cv2.setUseOptimized(True)
cv2.setNumThreads(4)

capture = cv2.VideoCapture()
assert capture.open('F:/aar/video/SFY/0.mp4')
frame = np.zeros(shape=[int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                        int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        3], dtype=np.uint8)

ret, frame = capture.read()
rect = cv2.selectROI('Choose object', frame, False, False)
tracker = kcf.KCFTracker(True, True, True, True)
r = [rect[0] + rect[2], rect[1] + rect[3]]
tracker.trackerInit([rect[0], rect[1], rect[2], rect[3]], frame)

count = 0
while True:
    ret, frame = capture.read()
    if not ret:
        print('finish!')
        break

    t_start = time.time()
    rect = tracker.trackerUpdate(frame)
    t_stop = time.time()
    fps = int(1.0/(t_stop - t_start))
    rect = list(map(int, rect))
    cv2.rectangle(frame, (rect[0], rect[1]), (rect[0]+ rect[2], rect[1] + rect[3]), (0, 255, 255), 2)
    cv2.putText(frame, '#' + str(count + 1), (64, 64), 1, 1, (255, 0, 0))
    cv2.putText(frame, '{}fps'.format(fps), (64, 64+30), 1, 1, (255, 0, 0))
    count += 1
    cv2.imshow('kcf', frame)
    if cv2.waitKey(33) == 'q':
        break

