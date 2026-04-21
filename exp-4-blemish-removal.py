import cv2
import numpy as np

# Load the image
img = cv2.imread('exp-4-original.jpg')

# Create an empty mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Mouse callback to mark blemishes
def mark_blemish(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(mask, (x, y), 10, 255, -1)   # mark blemish
        cv2.circle(img_display, (x, y), 10, (0,0,255), 1)

# Display window
img_display = img.copy()
cv2.namedWindow("Mark Blemishes")
cv2.setMouseCallback("Mark Blemishes", mark_blemish)

print("Left click on blemishes. Press 'i' to inpaint, 'q' to quit.")

while True:
    cv2.imshow("Mark Blemishes", img_display)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('i'):   # apply inpainting
        result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        cv2.imshow("Blemish Removed", result)

    elif key == ord('q'):
        break

cv2.destroyAllWindows()