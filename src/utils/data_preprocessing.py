# This file is responsible for preprocessing the keypoint data (from PoseNet and Mediapipe) before feeding it into the model for pose classification or correction.

import numpy as np

def normalize_keypoints(keypoints, image_size=(192, 192)):
    """
    Normalize the keypoints by image dimensions to ensure consistency.
    :param keypoints: A list of keypoints (x, y, z or just x, y).
    :param image_size: Tuple representing the image size (width, height).
    :return: Normalized keypoints.
    """
    width, height = image_size
    normalized_keypoints = []

    for kp in keypoints:
        normalized_keypoints.append([
            kp[0] / width,  # Normalize x by image width
            kp[1] / height,  # Normalize y by image height
            kp[2] if len(kp) == 3 else 0.0  # If z exists, keep it, otherwise use 0.0
        ])

    return np.array(normalized_keypoints)


def flatten_keypoints(keypoints, expected_size=51):
    """
    Flatten the keypoints and ensure they are of fixed size by padding or truncating.
    :param keypoints: List of keypoints from PoseNet/Mediapipe (body, hands, face).
    :param expected_size: The expected number of keypoints in the model input (default 51).
    :return: A 1D numpy array with the fixed size.
    """
    flattened = np.array(keypoints).flatten()

    # Pad with zeros or truncate to match the expected size
    if len(flattened) < expected_size:
        flattened = np.pad(flattened, (0, expected_size - len(flattened)), mode='constant')
    elif len(flattened) > expected_size:
        flattened = flattened[:expected_size]

    return flattened