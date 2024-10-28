# # Code for loading and using Yoga pose classification model

# import numpy as np
# # from tensorflow import load_model

# import tensorflow as tf

# # Path to the directory containing the 'saved_model.pb' file
# model_path = r"D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models"

# # Load the model from the path
# model = tf.saved_model.load(model_path)

# class YogaPoseClassifier:
#     def __init__(self, model_path):
#         """
#         Initialize the classifier by loading the pre-trained model.
        
#         :param model_path: Path to the pre-trained yoga pose classification model.
#         """
#         self.model = load_model(model_path)


#     def preprocess_keypoints(self, keypoints):
#         """
#         Preprocess keypoints extracted from PoseNet or Mediapipe to be compatible with the model.
        
#         :param keypoints: Dictionary or list of keypoints from PoseNet or Mediapipe.
#         :return: A flattened array of keypoints, ready for model input.
#         """
#         # If using Mediapipe, use body keypoints (since face/hands are not used in classification)
#         if isinstance(keypoints, dict) and 'body' in keypoints:
#             keypoints = keypoints['body']

#         # Flatten the keypoints into a 1D array if required by the model
#         flattened_keypoints = np.array(keypoints).flatten()
        
#         # If needed, pad or truncate keypoints to a fixed size (e.g., 51 for 17 keypoints in PoseNet)
#         if len(flattened_keypoints) < 51:
#             flattened_keypoints = np.pad(flattened_keypoints, (0, 51 - len(flattened_keypoints)))
#         elif len(flattened_keypoints) > 51:
#             flattened_keypoints = flattened_keypoints[:51]
        
#         return np.array([flattened_keypoints])
    


#     def classify_pose(self, keypoints):
#         """
#         Classify the yoga pose based on the keypoints from PoseNet or Mediapipe.
        
#         :param keypoints: The input keypoints (from PoseNet or Mediapipe) to classify.
#         :return: The predicted yoga pose class and the confidence score.
#         """
#         input_data = self.preprocess_keypoints(keypoints)  # Preprocess keypoints to match model input
#         prediction = self.model.predict(input_data)  # Get model prediction
        
#         return np.argmax(prediction), np.max(prediction)  # Return the class and confidence score

# Code for loading and using Yoga pose classification model
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Path to the directory containing the 'saved_model.pb' file
model_path = r"D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models"

# Load the MoveNet model
model = hub.KerasLayer("https://tfhub.dev/google/movenet/singlepose/lightning/4")



class YogaPoseClassifier:
    def __init__(self, model_path):
        """
        Initialize the classifier by loading the pre-trained model.
        
        :param model_path: Path to the pre-trained yoga pose classification model.
        """
        # Load the TensorFlow saved model
        self.model =  tf.compat.v2.saved_model.load(model_path)
        # Extract the serving signature to make predictions
        self.predict_fn = self.model.signatures["serving_default"]

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
        
        return np.array([flattened_keypoints])  # Return as a batch of one sample

    def classify_pose(self, keypoints):
        """
        Classify the yoga pose based on the keypoints from PoseNet or Mediapipe.
        
        :param keypoints: The input keypoints (from PoseNet or Mediapipe) to classify.
        :return: The predicted yoga pose class and the confidence score.
        """
        input_data = self.preprocess_keypoints(keypoints)  # Preprocess keypoints to match model input

        # Prepare input for the model: ensure it's a tensor
        input_tensor = tf.convert_to_tensor(input_data, dtype=tf.float32)

        # Get model prediction using the predict function from the saved model
        prediction = self.predict_fn(input_tensor)

        # Extract class and confidence from the prediction result
        predicted_class = np.argmax(prediction['Identity:0'].numpy())  # Replace "dense" with actual output layer name
        confidence_score = np.max(prediction['Identity:0'].numpy())  # Replace "dense" with actual output layer name
        
        return predicted_class, confidence_score


