import cv2
import numpy as np

# Load YOLOv7-tiny model with the configuration and weights
net = cv2.dnn.readNetFromDarknet('ASSIST.cfg', 'ASSIST.weights')

# Load the COCO class labels (80 classes including 'person')
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Function to detect humans using YOLOv7-tiny
def detect_humans(frame):
    (h, w) = frame.shape[:2]

    # Create a blob from the frame (resize to 416x416)
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Get the names of the output layers
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # Perform the forward pass and get detections
    detections = net.forward(output_layers)

    boxes = []
    confidences = []
    classIDs = []

    # Loop over each detection
    for output in detections:
        for detection in output:
            scores = detection[5:]  # Skip the first 5 elements (box coordinates)
            classID = np.argmax(scores)  # Get the class with the highest score
            confidence = scores[classID]

            # Filter out weak detections (confidence > 0.5)
            if confidence > 0.5 and classes[classID] == "person":
                # YOLO returns the center (x, y) coordinates, width, and height
                box = detection[0:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")

                # Get the top-left corner coordinates
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply Non-Maximum Suppression (NMS) to suppress overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw the bounding boxes and labels
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            # Draw the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Draw the label
            text = f"Person: {confidences[i]:.2f}"
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame
