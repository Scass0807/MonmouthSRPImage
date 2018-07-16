
import cv2
from datetime import datetime
import numpy as np
from threading import Thread 

class Webcam:

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.current_frame = self.video_capture.read()[1]

    # create thread for capturing images
    def start(self):
        Thread(target=self._update_frame, args=()).start()

    def _update_frame(self):
        while(True):
            self.current_frame = self.video_capture.read()[1]

    # get the current frame
    def get_current_frame(self):
        return self.current_frame
    
webcam = Webcam()
webcam.start()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((7*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:7].T.reshape(-1,2)
objpoints = []
imgpoints = []
i = 0

while i < 100:
    image = webcam.get_current_frame()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9,7), None)    
    print (ret)

    if ret == True:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)       
        imgpoints.append(corners)
        objpoints.append(objp)
        cv2.drawChessboardCorners(image, (9,7), corners,ret)
        i += 1


    cv2.imshow('grid', image)
    cv2.waitKey(1000)

cv2.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
np.savez("webcam_calibration_ouput_2", ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
