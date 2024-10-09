# Code to run PoseNet and extract keypoints
# posenet(15 keypoints)
import cv2
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub



# Load the PoseNet model from TensorFlow Hub (pretrained)
model = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")

def get_posenet_keypoints(image):
    """
    Extract keypoints using PoseNet for basic body poses (16 keypoints).
    :param image: Input image for pose estimation.
    :return: List of keypoints for the body (nose, shoulders, elbows, hips, knees, etc.).
    """
    input_image = cv2.resize(image, (192, 192))  # Resize image to match model input
    input_image = input_image.astype(np.float32) / 255.0  # Normalize image
    input_image = np.expand_dims(input_image, axis=0)  # Expand dimensions for batch size
    keypoints = model(input_image)

    # Extract keypoints from model output
    keypoints = keypoints['output_0'].numpy()[0]
    return keypoints