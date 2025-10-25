import cv2
import image_to_hsv as i2h
import filter_image as filter
import morph_and_moments as mm
import draw_rectangle as draw

cap = cv2.VideoCapture(0)

while True:
    frame = i2h.image_from_cam(cap, 640, 480)
    if frame is None:
        break

    hsv = i2h.to_hsv(frame)
    mask = filter.red_mask(hsv)
    morph = mm.morph_transform(mask)
    
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                objects.append({"cx": cx, "cy": cy, "area": area, "contour": cnt})

    frame = draw.draw_rectangles(frame, objects)

    cv2.imshow("трекинг красного", frame)
    cv2.imshow("маска", morph)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
