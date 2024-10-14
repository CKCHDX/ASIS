ASSIST | Artificial Safety Security Intelligence Systems Technology

The ASSIST system is a real-time security surveillance solution designed to detect various threats and enhance safety. It integrates multiple advanced detection techniques, which work together to provide comprehensive monitoring. Here's an overview of its main components:

1. Face Detection: The system uses a pre-trained model to detect faces in the video feed. It converts each frame to grayscale and identifies faces using the Haar Cascade algorithm. When a face is detected, it draws a box around the person’s face, making it easy to track individuals of interest.


2. Hostile Object Detection: The system is equipped to identify dangerous objects like knives and guns. Using a deep learning model (YOLOv7-tiny), it analyzes frames from the video to find objects that match these categories. Once a weapon is detected, the system highlights it with a red bounding box, alerting security personnel to a potential threat.


3. Human Detection: To monitor the presence of people in the area, the system uses another YOLOv7-tiny model, which is specifically trained to detect humans. It identifies individuals in the video and outlines them with a box, helping the system keep track of everyone within the monitored space.


4. Motion Detection: This feature is responsible for detecting movement. By comparing differences between consecutive video frames, it can spot motion and highlight areas where activity is occurring. If significant movement is detected, it triggers further analysis to check for faces, humans, or hostile objects.


5. System Integration: All these components work together seamlessly. The system first checks for motion—if any is detected, it activates face, human, and object detection to assess the situation. This layered approach ensures that only relevant frames are analyzed, optimizing performance. The final processed video, showing all detected elements, is displayed to the user for real-time monitoring.



The ASSIST system is built to provide robust security by detecting potential dangers and suspicious activities, making it an effective tool for surveillance in high-risk environments.

