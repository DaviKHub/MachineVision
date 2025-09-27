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
