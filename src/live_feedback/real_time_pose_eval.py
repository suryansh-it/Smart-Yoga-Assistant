# Code for real-time evaluation and feedback

# This script handles real-time evaluation of yoga poses, allowing fallback
# between PoseNet and Mediapipe for keypoint extraction

from pose_estimation.posenet_integration import get_posenet_keypoints
from pose_estimation.mediapipe_integration import get_mediapipe_keypoints
from live_feedback.feedback_utils import give_feedback

def evaluate_pose(image, use_posenet=True):
    """
    Evaluate yoga pose by extracting keypoints and providing feedback.
    
    :param image: Input image frame from the webcam.
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    :return: Feedback based on the pose evaluation.
    """

    if use_posenet:
        keypoints = get_posenet_keypoints(image)
    else:
        keypoints = get_mediapipe_keypoints(image)

    if keypoints:
        # Process keypoints and give feedback
        feedback = give_feedback(keypoints)
        return feedback
    return "No keypoints detected."