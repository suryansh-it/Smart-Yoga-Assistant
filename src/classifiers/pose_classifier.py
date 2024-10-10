# Code for loading and using Yoga pose classification model


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class YogaPoseClassifier:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def classify_pose(self, keypoints):
        input_data = np.array([keypoints])  # Input keypoints to model
        prediction = self.model.predict(input_data)
        return np.argmax(prediction), np.max(prediction)  # Return class and confidence

