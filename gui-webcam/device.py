import numpy as np
import cv2

import time
import os
import threading

class Camera:
    def __init__(self, cam_num=0):
        self.cam_num = cam_num
        self.cap = None
        self.frame = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)
        print("started")

    def get_frame(self):
        self.ret, self.frame = self.cap.read()
        if self.ret: 
            return (self.ret,self.frame)
        else:
            return (self.ret, None)

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print("closed")

        
    def record(self):
        if self.ret == 0:
            print("record error")
            return
        print("recording...")
        if not os.path.exists("record\\"):
            os.makedirs("record\\")
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter("record\\video-"+time.strftime("%Y%m%d-%H%M%S")+".avi", fourcc, 25.0, (640,480))

        while True:
            out.write(self.frame)
            if cv2.waitKey(0) & 0xFF == ord('s'):
                break
        
        out.release()
        print("video saved...")

    def capture(self):
        if self.ret:
            if not os.path.exists("capture\\"):
                os.makedirs("capture\\")
            cv2.imwrite("capture\\photo-"+time.strftime("%Y%m%d-%H%M%S")+".jpg", self.frame)



    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)


if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter("record\\video-"+time.strftime("%Y%m%d-%H%M%S")+".avi", fourcc, 25.0, (640,480))

    while(True):
        ret, frame = cam.get_frame()
        k = cv2.waitKey(1) & 0xFF
        if ret:
            cv2.imshow('frame',frame)
            if k == ord('q'): # q 키 눌러야 꺼짐
                break
            elif k == ord('c'): # c 키 누르면 캡쳐
                cam.capture()
            elif k == ord('r'): # r 키 누르면 녹화 => s 키 누르면 중지
                pass
    cam.close()
