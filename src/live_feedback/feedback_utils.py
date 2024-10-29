


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

# Utility functions for giving pose correction feedback
def give_feedback(keypoints):
    """
    Provide real-time feedback on yoga poses based on extracted keypoints.
    
    :param keypoints: A dictionary or list of keypoints extracted from PoseNet or Mediapipe.
    :return: A string with feedback for the user.
    """
    feedback = "Pose feedback: "
    
    if keypoints.any():  # Checking if there are valid keypoints
        
        # Ensure body keypoints are available
        if 'body' in keypoints:
            body_keypoints = keypoints['body']
            
            # Keep back straight
            feedback += "Keep your back straight. "
            
            # Check shoulder alignment
            if abs(body_keypoints[5][1] - body_keypoints[6][1]) > 0.05:
                feedback += "Align your shoulders. "
            else:
                feedback += "Shoulders are aligned. "
            
            # Check hip alignment
            if abs(body_keypoints[11][1] - body_keypoints[12][1]) > 0.05:
                feedback += "Align your hips. "
            
            # Example: Additional arm and leg position check
            if abs(body_keypoints[7][1] - body_keypoints[8][1]) > 0.1:
                feedback += "Straighten your left arm. "
            if abs(body_keypoints[15][1] - body_keypoints[16][1]) > 0.1:
                feedback += "Align your legs evenly. "
        
        # Use separate conditions for 17-point keypoints
        elif len(keypoints) == 17:
            if abs(keypoints[5][0] - keypoints[6][0]) > 0.1:
                feedback += "Raise your left shoulder slightly. "
            else:
                feedback += "Your shoulders look balanced. "
    
    else:
        feedback = "No keypoints detected. Adjust your position."

    return feedback
