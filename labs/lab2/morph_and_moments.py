import cv2
import numpy as np

def morph_transform(mask, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   # удаляет шумы
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)  # заполняет пробелы
    return closed


def find_objects(mask, area_threshold=500):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > area_threshold:
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                result.append({"cx": cx, "cy": cy, "area": area})
    return result
