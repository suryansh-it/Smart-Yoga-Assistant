# Utility functions for giving pose correction feedback


def give_feedback(keypoints):
    """
    Provide feedback on yoga poses based on extracted keypoints.
    
    :param keypoints: A dictionary of keypoints extracted from PoseNet or Mediapipe.
    :return: A string with feedback for the user.
    """
    # Example feedback logic (simplified):
    # Check the alignment of shoulders, hips, and knees for common yoga postures.