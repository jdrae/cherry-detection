import numpy as np
import cv2


class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.cap = None
        self.frame = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)
        print("started")

    def get_frame(self):
        ret, self.frame = self.cap.read()
        if ret:
            cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        return (ret, self.frame)

    #custom
    def convert_frame(self):
        pass

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print("closed")


    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)


if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    while(True):
        ret, frame = cam.get_frame()
        if ret:
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cam.close()
