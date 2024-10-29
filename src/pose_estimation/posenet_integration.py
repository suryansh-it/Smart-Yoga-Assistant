# import cv2
# import tensorflow as tf
# import numpy as np
# import tensorflow_hub as hub

# # Load the PoseNet model from TensorFlow Hub (pretrained)
# model = hub.KerasLayer("https://tfhub.dev/google/movenet/singlepose/lightning/4")
# movenet = model.signatures['serving_default']  # Get the callable model function

# def get_posenet_keypoints(image):
#     """
#     Extract keypoints using PoseNet for basic body poses (16 keypoints).
#     :param image: Input image for pose estimation.
#     :return: List of keypoints for the body (nose, shoulders, elbows, hips, knees, etc.).
#     """
#     # Resize and prepare the input image
#     input_image = cv2.resize(image, (192, 192))  # Resize image to match model input
#     input_image = input_image.astype(np.float32) / 255.0  # Normalize image
#     input_image = np.expand_dims(input_image, axis=0)  # Expand dimensions for batch size

#     # Create TensorFlow tensor
#     input_tensor = tf.convert_to_tensor(input_image)

#     input_tensor = tf.cast(input_tensor, tf.int32)  # Cast to int32

#     # Run inference
#     keypoints_output = movenet(input_tensor)

#     # Extract keypoints from model output
#     keypoints = keypoints_output['output_0'].numpy()[0]
#     return keypoints

# posenet integration

import cv2
import tensorflow as tf
import numpy as np

# Path to the locally saved MoveNet model
model_path = r"D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models"

class PoseNet:
    def __init__(self, model_path):
        # Load the model using tf.saved_model.load()
        self.model = tf.saved_model.load(model_path)
        self.predict_fn = self.model.signatures['serving_default']

    def get_posenet_keypoints(self, image):
        """
        Extract keypoints using PoseNet for body poses (16 keypoints).
        :param image: Input image for pose estimation.
        :return: List of keypoints for the body.
        """
        input_image = cv2.resize(image, (192, 192))
        input_image = input_image.astype(np.float32) / 255.0
        input_image = np.expand_dims(input_image, axis=0)
        input_tensor = tf.convert_to_tensor(input_image)
        keypoints_output = self.predict_fn(input_tensor)
        keypoints = keypoints_output['output_0'].numpy()[0]
        return keypoints

# Instantiate PoseNet
posenet_model = PoseNet(model_path)
