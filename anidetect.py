import cv2
import numpy as np
import tensorflow as tf

# Path to the saved model
model_path = r"C:\Users\ANANDA KRISHNAN.M\Desktop\python projects\animal detection\ssd_mobilenet_v2_coco\saved_model"

# Load the model
print("Loading model...")
try:
    detect_fn = tf.saved_model.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Define COCO classes for animals and people
target_classes = {
    1: "person",
    16: "cat", 17: "dog", 18: "horse", 19: "sheep", 20: "cow",
    21: "elephant", 22: "bear", 23: "zebra", 24: "giraffe",
    15: "bird"
}

# Start video capture
cap = cv2.VideoCapture(0)  # 0 for default webcam
if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resize frame to model's input size (e.g., 300x300 for SSD)
    input_frame = cv2.resize(frame, (300, 300))
    input_tensor = tf.convert_to_tensor(input_frame, dtype=tf.uint8)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Run detection
    try:
        detections = detect_fn(input_tensor)
    except Exception as e:
        print(f"Error during detection: {e}")
        break

    # Extract detection details
    bboxes = detections["detection_boxes"].numpy()[0]
    scores = detections["detection_scores"].numpy()[0]
    class_ids = detections["detection_classes"].numpy()[0].astype(int)

    height, width, _ = frame.shape

    for i in range(len(scores)):
        if scores[i] > 0.5:  # Detection confidence threshold
            class_id = class_ids[i]
            if class_id in target_classes:
                ymin, xmin, ymax, xmax = bboxes[i]
                (left, top, right, bottom) = (xmin * width, ymin * height, xmax * width, ymax * height)

                # Draw bounding box and label
                cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
                label = f"{target_classes[class_id]}: {scores[i]:.2f}"
                cv2.putText(frame, label, (int(left), int(top) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Wild Animal and Person Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
