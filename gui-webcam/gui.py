from device import Camera

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFrame
from PyQt5.QtCore import QSize, QRect, Qt, QThread, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon

import sys

class StartWindow(QMainWindow):
    def __init__(self, cam_num = 0):
        super().__init__()
        self.camera = Camera(cam_num)

        self.init_gui()
        self.set_timer()

        self.camera.initialize()
        self.timer.start(1)

    def init_gui(self):
        # main window settings
        window_width = 700
        window_height = 580
        self.resize(window_width, window_height)
        self.setMinimumSize(QSize(window_width,window_height))
        self.setMaximumSize(QSize(window_width,window_height))
        self.setWindowTitle("Zucchini")
        # self.setWindowIcon(QIcon("icon.png"))

        self.centralWidget = QWidget(self)
        self.centralWidget.resize(window_width,window_height)

        # webcam widget
        self.label_img = QLabel(self.centralWidget)
        self.label_img.setGeometry(QRect(30, 50, 640, 480))
        self.label_img.setFrameShape(QFrame.Box)
        self.label_img.setText("Loading...")

        # buttons
        self.btn_capture = QPushButton("capture",self.centralWidget)
        self.btn_capture.setGeometry(QRect(240, 540, 100, 30))
        self.btn_record = QPushButton("record",self.centralWidget)
        self.btn_record.setGeometry(QRect(360, 540, 100, 30))


    def set_timer(self):
        # timer to update frame
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def update_frame(self):
        ret, self.frame = self.camera.get_frame()
        if ret:
            QImg = QImage(self.frame.data, self.frame.shape[1], self.frame.shape[0], QImage.Format_RGB888)
            pixMap = QPixmap.fromImage(QImg)
            self.label_img.setPixmap(pixMap)
        else:
            self.label_img.setText("Cannot load camera")
    



if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exit(app.exec_())