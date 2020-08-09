from device import Camera
from gui import StartWindow

from PyQt5.QtWidgets import QApplication

import os
import cv2
import numpy as np
import tensorflow as tf

# log settings 
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# gpu settings
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    print(e)

# yolo settings
from yolov3.myyolov3 import Create_Yolo
from yolov3.utils import load_yolo_weights, detect_realtime
from yolov3.myconfigs import *

Darknet_weights = YOLO_V3_WEIGHTS
yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE)
load_yolo_weights(yolo, Darknet_weights)

# start gui application
app = QApplication([])
start_window = StartWindow(yolo, 0)
start_window.show()
app.exit(app.exec_())