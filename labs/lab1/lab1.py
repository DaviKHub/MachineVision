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

def task4():
    video = cv2.VideoCapture('../res/vids/video1.mp4', cv2.CAP_ANY)
    ret, frame = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("../res/vids/video1.avi", fourcc, fps, (w, h))
    while (True):
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow('Driving', frame)
        video_writer.write(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
