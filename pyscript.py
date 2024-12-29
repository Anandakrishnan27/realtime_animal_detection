import tensorflow as tf
import os

# Model path
model_path = r"C:\Users\ANANDA KRISHNAN.M\Desktop\python projects\animal detection\ssd_mobilenet_v2_coco\saved_model"

# Check if the path exists
if not os.path.exists(model_path):
    print("Error: Model path does not exist.")
else:
    print("Model path exists. Attempting to load the model...")

    try:
        detect_fn = tf.saved_model.load(model_path)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
