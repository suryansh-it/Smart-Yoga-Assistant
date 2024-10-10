# Code for loading and using Yoga pose classification model

import tensorflow as tf

class PoseClassifier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)