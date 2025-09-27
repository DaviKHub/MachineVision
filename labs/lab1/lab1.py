# task1
import cv2

def task2():
    img_1 = cv2.imread("../../res/pics/1.jpg", flags=0)
    cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
    cv2.imshow('image_1', img_1)
    img_2 = cv2.imread("../../res/pics/2.png", flags=-1)
    cv2.namedWindow("image_2", cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image_2', img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task3():
    cap = cv2.VideoCapture('../../res/vids/video1.mp4', cv2.CAP_ANY)
    ret, frame = cap.read()
    while frame is not None:
        if not (ret):
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
