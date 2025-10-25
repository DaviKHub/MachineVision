import cv2

def draw_rectangles(frame, objects, color=(0, 0, 0), thickness=2):
    for obj in objects:
        x, y, w, h = cv2.boundingRect(obj["contour"])
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
        cv2.circle(frame, (obj["cx"], obj["cy"]), 4, color, -1)
    return frame
