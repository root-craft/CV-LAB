import cv2
import numpy as np

# Load image
img = cv2.imread("image.jpg")
mask = np.zeros(img.shape[:2], dtype=np.uint8)
display = img.copy()


# Mouse callback to mark blemish
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(display, (x, y), 10, (0, 0, 255), -1)  # show mark
        cv2.circle(mask, (x, y), 10, 255, -1)  # mask


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_circle)

# Show image and take input
while True:
    cv2.imshow("Image", display)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):  # run inpaint
        result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        cv2.imshow("Result", result)

    elif key == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
