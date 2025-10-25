import cv2
import image_to_hsv as i2h
import filter_image as filter
import morph_and_moments as mm
import draw_rectangle as draw

def main():
    cap = cv2.VideoCapture(0)

    while True:
        frame = i2h.image_from_cam(cap, 640, 480)
        if frame is None:
            break

        hsv = i2h.to_hsv(frame)
        mask = filter.red_mask(hsv)
        morph = mm.morph_transform(mask)
        objects = mm.find_objects(morph)
        frame = draw.draw_rectangles(frame, objects)

        cv2.imshow("Red tracking", frame)
        cv2.imshow("Mask", morph)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
