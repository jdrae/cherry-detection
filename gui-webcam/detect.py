import numpy as np
import cv2

# yolo settings
net = cv2.dnn.readNet("zuc/z-yolo.weights", "zuc/z-config.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

min_confidence = 0.5

className = "zucchini"
color = (100, 0, 100)
font = cv2.FONT_HERSHEY_PLAIN
width = 0
height = 0

def detect_zucchini(frame):
    print("detect...")
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > min_confidence:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                label = '{} {:,.2%}'.format(className, confidence)

                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 10), font, 1, color, 2)
    return frame


if __name__ == '__main__':
    vs = cv2.VideoCapture('zuc/z-video.avi')
    if not vs.isOpened:
        print('Cannot load video')
        exit(0)
    
    width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = vs.read()
        if frame is None:
            print('No frame')
            vs.release()
            break
        cv2.imshow('', detect_zucchini(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vs.release()
    cv2.destroyAllWindows()