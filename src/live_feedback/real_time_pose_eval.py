

# This script handles real-time evaluation of yoga poses, allowing fallback
# between PoseNet and Mediapipe for keypoint extraction

# from src.pose_estimation.posenet_integration import get_posenet_keypoints
# from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
# from src.live_feedback.feedback_utils import give_feedback

# def evaluate_pose(image, use_posenet=True):
#     """
#     Evaluate yoga pose by extracting keypoints and providing feedback.
    
#     :param image: Input image frame from the webcam.
#     :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
#     :return: Feedback based on the pose evaluation.
#     """

#     if use_posenet:
#         keypoints = get_posenet_keypoints(image)
#     else:
#         keypoints = get_mediapipe_keypoints(image)

#     # if keypoints:
#     #     # Process keypoints and give feedback
#     #     feedback = give_feedback(keypoints)
#     #     return feedback
#     # return "No keypoints detected."

#     keypoints = get_posenet_keypoints(image)  # Assuming this returns a NumPy array or tensor
#     if keypoints.any():  # Check if any keypoints exist
#         # Proceed with pose evaluation logic
#         # Process keypoints and give feedback
#         feedback = give_feedback(keypoints)
        
#     else:
#         # Handle the case where no keypoints are detected
#         feedback= "No keypoints detected."
#     return feedback

# Code for real-time evaluation and feedback

import tensorflow as tf
import numpy as np
from src.pose_estimation.posenet_integration import PoseNet
# from src.pose_estimation.posenet_integration import get_posenet_keypoints
from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
from src.live_feedback.feedback_utils import give_feedback


model_path = r'D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models'

# PoseNet class expects the model_path parameter when creating an instance
posenet_instance = PoseNet(model_path=model_path)

def evaluate_pose(image, use_posenet=True):
    """
    Evaluate yoga pose by extracting keypoints and providing feedback.
    
    :param image: Input image frame from the webcam.
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    :return: Feedback based on the pose evaluation.
    """
    # Get keypoints from PoseNet or Mediapipe
    try:
        keypoints = posenet_instance.get_posenet_keypoints(image) if use_posenet else get_mediapipe_keypoints(image)

                # Log extracted keypoints for debugging
        print("Extracted Keypoints:", keypoints)

        # Check if keypoints are detected and not empty
        if isinstance(keypoints, np.ndarray) and keypoints.any():
            feedback = give_feedback(keypoints)
        else:
            feedback = "No keypoints detected."

    except Exception as e:
        print(f"Error in evaluating pose: {e}")
        feedback = "Error in pose evaluation."

    return feedback
