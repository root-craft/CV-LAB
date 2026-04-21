# Import Required Libraries
import cv2
import sys

# Load the Video
video_path = r'D:\SREC\SEM 6\Computer Vision\Rec\exp-10-sample.mp4'   # Change to 0 for webcam

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")

# Read First Frame
ret, frame = cap.read()

if not ret:
    print("Error: Failed to read video.")
    cap.release()
    sys.exit()

# Display first frame for ROI selection
cv2.imshow("First Frame", frame)
cv2.waitKey(1)

# Select ROI (Region of Interest)
print("Select the object to track and press ENTER or SPACE.")
bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)

cv2.destroyWindow("Select Object")

# Create and Initialize CSRT Tracker
# Create CSRT tracker
tracker = cv2.TrackerCSRT_create()

# Initialize tracker with first frame and bounding box
tracker.init(frame, bbox)

print("Tracking started...")

# Perform Object Tracking
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Update tracker
    success, bbox = tracker.update(frame)
    
    if success:
        x, y, w, h = [int(i) for i in bbox]
        
        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    cv2.imshow("Object Tracking - CSRT", frame)
    
    # Exit on ESC key
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break


# Release Resources
cap.release()
cv2.destroyAllWindows()
print("Tracking finished.")