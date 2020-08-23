'''
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
'''

import numpy as np
import cv2
from threading import Thread

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
ret = 0
frame = None

def record():
	global ret, frame
	print("recording...")
	while(cap.isOpened()):
		if ret==True:
			out.write(frame)
			if cv2.waitKey(1) & 0xFF == ord('s'):
				print("record stopped")
				break
		else:
			break
	out.release()

def update():
	global ret, frame
	print("--start--")
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret==True:
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				print("--end--")
				break
		else:
			print("--end--")
			break

def printFrame():
	global ret, frame
	if ret:
		print("frame:",frame[0][0])
	else:
		print("no frame")

t1 = Thread(target=update)
t2 = Thread(target=printFrame)
t1.start()
t2.start()


cap.release()
cv2.destroyAllWindows()