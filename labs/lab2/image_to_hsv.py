import cv2

def image_from_cam(cap, w, h):
    cap.set(3, w)
    cap.set(4, h)
    ret, frame = cap.read()
    return frame if ret else None

def to_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
