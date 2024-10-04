import cv2
from motion_detection import detect_motion
from face_detection import detect_faces
from human_detection import detect_humans

# Initialize the camera
camera = cv2.VideoCapture(0)

# Initialize first frame for motion detection
first_frame = None

while True:
    # Capture the current frame
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Motion Detection
    frame_with_motion, first_frame = detect_motion(frame, first_frame)

    # If motion is detected, run other detections
    if frame_with_motion is not None:
        # Face Detection
        frame_with_faces = detect_faces(frame_with_motion)

        # Human Detection
        frame_with_humans = detect_humans(frame_with_faces)

        # Show the final output
        cv2.imshow("Security Feed", frame_with_humans)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()
