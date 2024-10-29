# This file is responsible for preprocessing the keypoint data (from PoseNet and Mediapipe)
# before feeding it into the model for pose classification or correction.

import numpy as np

def normalize_keypoints(keypoints, image_size=(192, 192)):
    """
    Normalize keypoints by image dimensions.
    :param keypoints: List of keypoints.
    :param image_size: Image size (width, height).
    :return: Normalized keypoints.
    """
    width, height = image_size
    normalized_keypoints = [
        [kp[0] / width, kp[1] / height, kp[2] if len(kp) == 3 else 0.0] for kp in keypoints
    ]
    return np.array(normalized_keypoints)

def flatten_keypoints(keypoints, expected_size=51):
    """
    Flatten keypoints and pad/truncate to match expected size.
    :param keypoints: List of keypoints.
    :param expected_size: Expected number of keypoints.
    :return: 1D numpy array with fixed size.
    """
    flattened = np.array(keypoints).flatten()
    if len(flattened) < expected_size:
        flattened = np.pad(flattened, (0, expected_size - len(flattened)), mode='constant')
    elif len(flattened) > expected_size:
        flattened = flattened[:expected_size]
    return flattened
