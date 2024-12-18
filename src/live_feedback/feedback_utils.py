


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
# def give_feedback(keypoints):
#     """
#     Provide real-time feedback on yoga poses based on extracted keypoints.
    
#     :param keypoints: A 3D array of keypoints extracted from PoseNet or Mediapipe.
#     :return: A string with feedback for the user.
#     """
#     feedback = "Pose feedback: "
#     confidence_threshold = 0.05  # Minimum confidence level to consider a keypoint valid
#     feedback_parts = []  # To accumulate individual feedback messages

#     # Check if keypoints are valid and contain 17 points
#     if keypoints is not None and len(keypoints[0]) == 17:
#         print("Processing Keypoints in give_feedback:", keypoints)  # Debugging line

#         # Shoulder alignment (indexes 5 and 6)
#         left_shoulder_y = keypoints[0][5][1]
#         right_shoulder_y = keypoints[0][6][1]
#         left_shoulder_conf = keypoints[0][5][2]
#         right_shoulder_conf = keypoints[0][6][2]

#         if left_shoulder_conf > confidence_threshold and right_shoulder_conf > confidence_threshold:
#             if abs(left_shoulder_y - right_shoulder_y) > 0.05:
#                 feedback_parts.append("Align your shoulders.")
#             else:
#                 feedback_parts.append("Shoulders are aligned.")

#         # Hip alignment (indexes 11 and 12)
#         left_hip_y = keypoints[0][11][1]
#         right_hip_y = keypoints[0][12][1]
#         left_hip_conf = keypoints[0][11][2]
#         right_hip_conf = keypoints[0][12][2]

#         if left_hip_conf > confidence_threshold and right_hip_conf > confidence_threshold:
#             if abs(left_hip_y - right_hip_y) > 0.05:
#                 feedback_parts.append("Align your hips.")

#         # Arm alignment (left arm indexes 7 and 9, right arm indexes 8 and 10)
#         left_elbow_y = keypoints[0][7][1]
#         left_wrist_y = keypoints[0][9][1]
#         left_elbow_conf = keypoints[0][7][2]
#         left_wrist_conf = keypoints[0][9][2]

#         if left_elbow_conf > confidence_threshold and left_wrist_conf > confidence_threshold:
#             if abs(left_elbow_y - left_wrist_y) > 0.1:
#                 feedback_parts.append("Straighten your left arm.")

#         right_elbow_y = keypoints[0][8][1]
#         right_wrist_y = keypoints[0][10][1]
#         right_elbow_conf = keypoints[0][8][2]
#         right_wrist_conf = keypoints[0][10][2]

#         if right_elbow_conf > confidence_threshold and right_wrist_conf > confidence_threshold:
#             if abs(right_elbow_y - right_wrist_y) > 0.1:
#                 feedback_parts.append("Straighten your right arm.")

#         # Leg alignment (left leg indexes 15 and 16, right leg indexes 13 and 14)
#         left_knee_y = keypoints[0][15][1]
#         left_ankle_y = keypoints[0][16][1]
#         left_knee_conf = keypoints[0][15][2]
#         left_ankle_conf = keypoints[0][16][2]

#         if left_knee_conf > confidence_threshold and left_ankle_conf > confidence_threshold:
#             if abs(left_knee_y - left_ankle_y) > 0.1:
#                 feedback_parts.append("Align your left leg evenly.")

#         right_knee_y = keypoints[0][13][1]
#         right_ankle_y = keypoints[0][14][1]
#         right_knee_conf = keypoints[0][13][2]
#         right_ankle_conf = keypoints[0][14][2]

#         if right_knee_conf > confidence_threshold and right_ankle_conf > confidence_threshold:
#             if abs(right_knee_y - right_ankle_y) > 0.1:
#                 feedback_parts.append("Align your right leg evenly.")

#     else:
#         feedback_parts.append("No keypoints detected. Adjust your position.")

#     # Combine feedback parts into a single message
#     feedback += " ".join(feedback_parts) if feedback_parts else "All good!"
#     print("Final Feedback:", feedback)  # Debugging line
#     return feedback


# Utility function for giving pose correction feedback
import numpy as np
def give_feedback(keypoints):
    """
    Provide real-time feedback on yoga poses based on extracted keypoints.

    :param keypoints: A 3D array of keypoints extracted from PoseNet or Mediapipe.
    :return: A string with feedback for the user.
    """
    # Define keypoint indices
    LEFT_HIP, RIGHT_HIP = 11, 12
    LEFT_SHOULDER, RIGHT_SHOULDER = 5, 6
    LEFT_WRIST, RIGHT_WRIST = 9, 10
    LEFT_ELBOW, RIGHT_ELBOW = 7, 8
    LEFT_KNEE, RIGHT_KNEE = 15, 13
    LEFT_ANKLE, RIGHT_ANKLE = 16, 14

    feedback = "Pose feedback: "
    confidence_threshold = 0.05
    feedback_parts = []

    # Ensure keypoints are in the expected format
    if keypoints is not None and len(keypoints[0]) == 17:
        print("Processing Keypoints in give_feedback:", keypoints)  # Debugging line

        # Helper function to check if a keypoint is valid
        def is_valid_keypoint(keypoint):
            return isinstance(keypoint, np.ndarray) and len(keypoint) == 3

        # Shoulder alignment
        if is_valid_keypoint(keypoints[0][LEFT_SHOULDER]) and is_valid_keypoint(keypoints[0][RIGHT_SHOULDER]):
            left_shoulder_y, left_shoulder_conf = keypoints[0][LEFT_SHOULDER][1], keypoints[0][LEFT_SHOULDER][2]
            right_shoulder_y, right_shoulder_conf = keypoints[0][RIGHT_SHOULDER][1], keypoints[0][RIGHT_SHOULDER][2]

            if left_shoulder_conf > confidence_threshold and right_shoulder_conf > confidence_threshold:
                if abs(left_shoulder_y - right_shoulder_y) > 0.05:
                    feedback_parts.append("Align your shoulders evenly.")
                else:
                    feedback_parts.append("Shoulders are aligned well.")

        # Hip alignment
        if is_valid_keypoint(keypoints[0][LEFT_HIP]) and is_valid_keypoint(keypoints[0][RIGHT_HIP]):
            left_hip_y, left_hip_conf = keypoints[0][LEFT_HIP][1], keypoints[0][LEFT_HIP][2]
            right_hip_y, right_hip_conf = keypoints[0][RIGHT_HIP][1], keypoints[0][RIGHT_HIP][2]

            if left_hip_conf > confidence_threshold and right_hip_conf > confidence_threshold:
                if abs(left_hip_y - right_hip_y) > 0.05:
                    feedback_parts.append("Align your hips.")
                else:
                    feedback_parts.append("Hips are aligned well.")

        # Arm alignment
        if is_valid_keypoint(keypoints[0][LEFT_ELBOW]) and is_valid_keypoint(keypoints[0][LEFT_WRIST]):
            left_elbow_y, left_wrist_y = keypoints[0][LEFT_ELBOW][1], keypoints[0][LEFT_WRIST][1]
            left_elbow_conf, left_wrist_conf = keypoints[0][LEFT_ELBOW][2], keypoints[0][LEFT_WRIST][2]

            if left_elbow_conf > confidence_threshold and left_wrist_conf > confidence_threshold:
                if abs(left_elbow_y - left_wrist_y) > 0.1:
                    feedback_parts.append("Straighten your left arm.")

        if is_valid_keypoint(keypoints[0][RIGHT_ELBOW]) and is_valid_keypoint(keypoints[0][RIGHT_WRIST]):
            right_elbow_y, right_wrist_y = keypoints[0][RIGHT_ELBOW][1], keypoints[0][RIGHT_WRIST][1]
            right_elbow_conf, right_wrist_conf = keypoints[0][RIGHT_ELBOW][2], keypoints[0][RIGHT_WRIST][2]

            if right_elbow_conf > confidence_threshold and right_wrist_conf > confidence_threshold:
                if abs(right_elbow_y - right_wrist_y) > 0.1:
                    feedback_parts.append("Straighten your right arm.")

        # Leg alignment
        if is_valid_keypoint(keypoints[0][LEFT_KNEE]) and is_valid_keypoint(keypoints[0][LEFT_ANKLE]):
            left_knee_y, left_ankle_y = keypoints[0][LEFT_KNEE][1], keypoints[0][LEFT_ANKLE][1]
            left_knee_conf, left_ankle_conf = keypoints[0][LEFT_KNEE][2], keypoints[0][LEFT_ANKLE][2]

            if left_knee_conf > confidence_threshold and left_ankle_conf > confidence_threshold:
                if abs(left_knee_y - left_ankle_y) > 0.1:
                    feedback_parts.append("Keep your left leg straight.")

        if is_valid_keypoint(keypoints[0][RIGHT_KNEE]) and is_valid_keypoint(keypoints[0][RIGHT_ANKLE]):
            right_knee_y, right_ankle_y = keypoints[0][RIGHT_KNEE][1], keypoints[0][RIGHT_ANKLE][1]
            right_knee_conf, right_ankle_conf = keypoints[0][RIGHT_KNEE][2], keypoints[0][RIGHT_ANKLE][2]

            if right_knee_conf > confidence_threshold and right_ankle_conf > confidence_threshold:
                if abs(right_knee_y - right_ankle_y) > 0.1:
                    feedback_parts.append("Keep your right leg straight.")

    else:
        feedback_parts.append("No keypoints detected. Adjust your position.")

    # Combine feedback parts into a single message
    feedback += " | ".join(feedback_parts) if feedback_parts else "All good!"
    print("Final Feedback:", feedback)  # Debugging line
    return feedback
