# Optional: Code to run Mediapipe (as fallback for pose estimation)
# mediapipe(33 keypoints with hands , feet and face)

import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh

pose = mp_pose.Pose()
hands = mp_hands.Hands()
face_mesh = mp_face_mesh.FaceMesh()

def get_mediapipe_keypoints(image):
    """
    Use Mediapipe to get 33 body keypoints (including facial, hands, feet).
    :param image: Input image for pose estimation.
    :return: A dictionary with body, hands, and face keypoints.
    """
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results_pose = pose.process(image_rgb)
    results_hands = hands.process(image_rgb)
    results_face = face_mesh.process(image_rgb)

    keypoints = {
        'body': [],
        'hands': [],
        'face': []
    }

    # Extract body pose keypoints
    if results_pose.pose_landmarks:
        keypoints['body'] = [
            [landmark.x, landmark.y, landmark.z] for landmark in results_pose.pose_landmarks.landmark
        ]

    # Extract hand keypoints
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            keypoints['hands'].append([
                [landmark.x, landmark.y, landmark.z] for landmark in hand_landmarks.landmark
            ])

    # Extract face mesh keypoints
    if results_face.multi_face_landmarks:
        keypoints['face'] = [
            [landmark.x, landmark.y, landmark.z] for landmark in results_face.multi_face_landmarks[0].landmark
        ]

    return keypoints