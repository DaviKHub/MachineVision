import cv2

def image_from_cam(cap, w, h):
    cap.set(3, w)
    cap.set(4, h)
    ret, frame = cap.read()
    if ret:
        return frame
    else:
        return None

def to_hsv(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img_hsv

cap = cv2.VideoCapture(0)
cv2.namedWindow("img_rgb", cv2.WINDOW_NORMAL)
cv2.namedWindow("img_hsv", cv2.WINDOW_NORMAL)

img = image_from_cam(cap, 640, 480)

if img is not None:
    cv2.imshow("img_rgb", img)
    cv2.imshow("img_hsv", to_hsv(img))
    cv2.waitKey(0)
else:
    print("Не удалось получить изображение с камеры")

cap.release()
cv2.destroyAllWindows()