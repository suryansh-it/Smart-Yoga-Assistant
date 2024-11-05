

# # This script handles real-time evaluation of yoga poses, allowing fallback
# # between PoseNet and Mediapipe for keypoint extraction

# # from src.pose_estimation.posenet_integration import get_posenet_keypoints
# # from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
# # from src.live_feedback.feedback_utils import give_feedback

# # def evaluate_pose(image, use_posenet=True):
# #     """
# #     Evaluate yoga pose by extracting keypoints and providing feedback.
    
# #     :param image: Input image frame from the webcam.
# #     :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
# #     :return: Feedback based on the pose evaluation.
# #     """

# #     if use_posenet:
# #         keypoints = get_posenet_keypoints(image)
# #     else:
# #         keypoints = get_mediapipe_keypoints(image)

# #     # if keypoints:
# #     #     # Process keypoints and give feedback
# #     #     feedback = give_feedback(keypoints)
# #     #     return feedback
# #     # return "No keypoints detected."

# #     keypoints = get_posenet_keypoints(image)  # Assuming this returns a NumPy array or tensor
# #     if keypoints.any():  # Check if any keypoints exist
# #         # Proceed with pose evaluation logic
# #         # Process keypoints and give feedback
# #         feedback = give_feedback(keypoints)
        
# #     else:
# #         # Handle the case where no keypoints are detected
# #         feedback= "No keypoints detected."
# #     return feedback

# # Code for real-time evaluation and feedback

# import tensorflow as tf
# import numpy as np
# from src.pose_estimation.posenet_integration import PoseNet
# # from src.pose_estimation.posenet_integration import get_posenet_keypoints
# from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
# from src.live_feedback.feedback_utils import give_feedback


# model_path = r'D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models'

# # PoseNet class expects the model_path parameter when creating an instance
# posenet_instance = PoseNet(model_path=model_path)

# def evaluate_pose(image, use_posenet=True):
#     """
#     Evaluate yoga pose by extracting keypoints and providing feedback.
    
#     :param image: Input image frame from the webcam.
#     :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
#     :return: Feedback based on the pose evaluation.
#     """
#     # Get keypoints from PoseNet or Mediapipe
#     try:
#         keypoints = posenet_instance.get_posenet_keypoints(image) if use_posenet else get_mediapipe_keypoints(image)

#                 # Log extracted keypoints for debugging
#         print("Extracted Keypoints:", keypoints)

#         # Check if keypoints are detected and not empty
#         if isinstance(keypoints, np.ndarray) and keypoints.any():
#             feedback = give_feedback(keypoints)
#         else:
#             feedback = "No keypoints detected."

#     except Exception as e:
#         print(f"Error in evaluating pose: {e}")
#         feedback = "Error in pose evaluation."

#     return feedback

# import tensorflow as tf
# import numpy as np
# from src.pose_estimation.posenet_integration import PoseNet
# from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
# from src.live_feedback.feedback_utils import give_feedback
# import cv2

# model_path = r'D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models'
# posenet_instance = PoseNet(model_path=model_path)

# def evaluate_pose(image, use_posenet=True):
#     """
#     Evaluate yoga pose by extracting keypoints and providing feedback.
    
#     :param image: Input image frame from the webcam.
#     :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
#     :return: Feedback and keypoints for further processing.
#     """
#     try:
#         keypoints = posenet_instance.get_posenet_keypoints(image) if use_posenet else get_mediapipe_keypoints(image)

#         # Log extracted keypoints for debugging
#         print("Extracted Keypoints:", keypoints)

#         # Check if keypoints are valid and not empty
#         if isinstance(keypoints, np.ndarray) and keypoints.size > 0:
#             feedback = give_feedback(keypoints)
#         else:
#             feedback = "No keypoints detected."
#             keypoints = np.array([])

#     except Exception as e:
#         print(f"Error in evaluating pose: {e}")
#         feedback = "Error in pose evaluation."
#         keypoints = np.array([])

#     return feedback, keypoints


import tensorflow as tf
import numpy as np
from src.pose_estimation.posenet_integration import PoseNet
from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
from src.live_feedback.feedback_utils import give_feedback
import cv2

model_path = r'D:/Dev/python/Flask/dev_flask/Smart-Yoga-Assistant/models'
posenet_instance = PoseNet(model_path=model_path)

def check_hip_alignment(keypoints):
    # Example hip alignment check
    return abs(keypoints[LEFT_HIP][1] - keypoints[RIGHT_HIP][1]) < 10  # Adjust threshold

def check_spine_alignment(keypoints):
    # Example spine alignment check
    shoulder_y = (keypoints[LEFT_SHOULDER][1] + keypoints[RIGHT_SHOULDER][1]) / 2
    hip_y = (keypoints[LEFT_HIP][1] + keypoints[RIGHT_HIP][1]) / 2
    return abs(shoulder_y - hip_y) < 20  # Adjust threshold

def check_arm_position(keypoints):
    # Example arm position check
    return keypoints[LEFT_WRIST][1] < keypoints[LEFT_SHOULDER][1] and keypoints[RIGHT_WRIST][1] < keypoints[RIGHT_SHOULDER][1]

def evaluate_pose(image, use_posenet=True):
    """
    Evaluate yoga pose by extracting keypoints and providing feedback.
    
    :param image: Input image frame from the webcam.
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    :return: Feedback and keypoints for further processing.
    """
    try:
        keypoints = posenet_instance.get_posenet_keypoints(image) if use_posenet else get_mediapipe_keypoints(image)

        # Log extracted keypoints for debugging
        print("Extracted Keypoints:", keypoints)

        # Check if keypoints are valid and not empty
        if isinstance(keypoints, np.ndarray) and keypoints.size > 0:
            feedback = []

            # Apply individual checks for feedback
            if check_hip_alignment(keypoints):
                feedback.append("Align your hips")
            if check_spine_alignment(keypoints):
                feedback.append("Keep your spine straight")
            if check_arm_position(keypoints):
                feedback.append("Extend your arms fully")

            # Join all feedback messages or set default if none
            feedback = " | ".join(feedback) if feedback else "Good posture"
        else:
            feedback = "No keypoints detected."
            keypoints = np.array([])

    except Exception as e:
        print(f"Error in evaluating pose: {e}")
        feedback = "Error in pose evaluation."
        keypoints = np.array([])

    return feedback, keypoints
