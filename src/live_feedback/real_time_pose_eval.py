# Code for real-time evaluation and feedback

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


from src.pose_estimation.posenet_integration import get_posenet_keypoints
from src.pose_estimation.mediapipe_integration import get_mediapipe_keypoints
from src.live_feedback.feedback_utils import give_feedback

def evaluate_pose(image, use_posenet=True):
    """
    Evaluate yoga pose by extracting keypoints and providing feedback.
    
    :param image: Input image frame from the webcam.
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    :return: Feedback based on the pose evaluation.
    """
    # Get keypoints from PoseNet or Mediapipe
    keypoints = get_posenet_keypoints(image) if use_posenet else get_mediapipe_keypoints(image)

    # Check if keypoints are detected
    if keypoints.any():  # Assuming keypoints is a NumPy array or tensor
        # Process keypoints and give feedback
        feedback = give_feedback(keypoints)
    else:
        feedback = "No keypoints detected."

    return feedback
