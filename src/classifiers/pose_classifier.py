# Code for loading and using Yoga pose classification model

import numpy as np
from tensorflow.keras.models import load_model

class YogaPoseClassifier:
    def __init__(self, model_path):
        """
        Initialize the classifier by loading the pre-trained model.
        
        :param model_path: Path to the pre-trained yoga pose classification model.
        """
        self.model = load_model(model_path)


    def preprocess_keypoints(self, keypoints):
        """
        Preprocess keypoints extracted from PoseNet or Mediapipe to be compatible with the model.
        
        :param keypoints: Dictionary or list of keypoints from PoseNet or Mediapipe.
        :return: A flattened array of keypoints, ready for model input.
        """
        # If using Mediapipe, use body keypoints (since face/hands are not used in classification)
        if isinstance(keypoints, dict) and 'body' in keypoints:
            keypoints = keypoints['body']

        # Flatten the keypoints into a 1D array if required by the model
        flattened_keypoints = np.array(keypoints).flatten()
        
        # If needed, pad or truncate keypoints to a fixed size (e.g., 51 for 17 keypoints in PoseNet)
        if len(flattened_keypoints) < 51:
            flattened_keypoints = np.pad(flattened_keypoints, (0, 51 - len(flattened_keypoints)))
        elif len(flattened_keypoints) > 51:
            flattened_keypoints = flattened_keypoints[:51]
        
        return np.array([flattened_keypoints])
    


    def classify_pose(self, keypoints):
        """
        Classify the yoga pose based on the keypoints from PoseNet or Mediapipe.
        
        :param keypoints: The input keypoints (from PoseNet or Mediapipe) to classify.
        :return: The predicted yoga pose class and the confidence score.
        """
        input_data = self.preprocess_keypoints(keypoints)  # Preprocess keypoints to match model input
        prediction = self.model.predict(input_data)  # Get model prediction
        
        return np.argmax(prediction), np.max(prediction)  # Return the class and confidence score