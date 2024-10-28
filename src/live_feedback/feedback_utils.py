# Utility functions for giving pose correction feedback


# def give_feedback(keypoints):
#     """
#     Provide feedback on yoga poses based on extracted keypoints.
    
#     :param keypoints: A dictionary of keypoints extracted from PoseNet or Mediapipe.
#     :return: A string with feedback for the user.
#     """
#     # Example feedback logic (simplified):
#     # Check the alignment of shoulders, hips, and knees for common yoga postures.

#     if keypoints:
#         # Assume we have 'body' keypoints for mediapipe, or a flat list for posenet
#         if 'body' in keypoints:
#             body_keypoints = keypoints['body']
#             feedback = "Keep your back straight."  # Example feedback

#             # Example: Check if shoulders are aligned
#             if abs(body_keypoints[5][1] - body_keypoints[6][1]) > 0.05:
#                 feedback += " Try aligning your shoulders."
#             else:
#                 feedback += " Your shoulders are aligned."

#             # Further feedback logic can be added here...
#             return feedback
        
#         elif len(keypoints) == 17:  # PoseNet returns 17 keypoints
#             feedback = "Ensure proper balance in your pose."
#             # Example: Simple comparison of left and right shoulder
#             if abs(keypoints[5][0] - keypoints[6][0]) > 0.1:
#                 feedback += " Raise your left shoulder to be in line."
#             else:
#                 feedback += " Your shoulders are aligned."
#             return feedback
#     return "No keypoints detected. Adjust your position."


def give_feedback(keypoints):
    """
    Provide feedback on yoga poses based on extracted keypoints.
    
    :param keypoints: A dictionary or list of keypoints extracted from PoseNet or Mediapipe.
    :return: A string with feedback for the user.
    """
    feedback = ""
    
    if keypoints.any():  # Checking if there are valid keypoints
        if 'body' in keypoints:
            body_keypoints = keypoints['body']
            feedback = "Keep your back straight."

            # Check if shoulders are aligned
            if abs(body_keypoints[5][1] - body_keypoints[6][1]) > 0.05:
                feedback += " Try aligning your shoulders."
            else:
                feedback += " Your shoulders are aligned."
        
        elif len(keypoints) == 17:
            feedback = "Ensure proper balance in your pose."
            if abs(keypoints[5][0] - keypoints[6][0]) > 0.1:
                feedback += " Raise your left shoulder to be in line."
            else:
                feedback += " Your shoulders are aligned."
    else:
        feedback = "No keypoints detected. Adjust your position."

    return feedback
