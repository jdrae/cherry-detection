import cv2
import threading
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class WindowClass(QtWidgets.QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.win = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.btn_start = QtWidgets.QPushButton("Camera On")
        self.btn_stop = QtWidgets.QPushButton("Camera Off")
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btn_start)
        self.vbox.addWidget(self.btn_stop)
        self.win.setLayout(self.vbox)

    def setLabel(self,ret, value):
        if ret:
            self.label.setPixmap(value)
        else:
            QtWidgets.QMessageBox.about(self.win, "Error", value)

class WorkThread(WindowClass):
    def __init__(self, gui):
        super.__init__()
        self.running = False
        self.cap = cv2.VideoCapture(0)
        self.gui.btn_start.clicked.connect(self.start)
        self.gui.btn_stop.clicked.connect(self.stop)

    def run(self):
        while self.running:
            ret, img = self.cap.read()
            width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            if ret:
                img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.gui.setLabel(1, pixmap)
            else:
                self.gui.setLabel(0, "Cannot read frame.")

        self.cap.release()
        print("Thread end.")

    def stop(self):
        self.running = False
        print("stoped..")

    def start(self):
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")

    def onExit(self):
        print("exit")
        self.stop()




app = QtWidgets.QApplication([])
myWindow = WindowClass()
thread = WorkThread(myWindow)
myWindow.show()
app.exec_()