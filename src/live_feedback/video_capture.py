# import cv2
# from .real_time_pose_eval import evaluate_pose

# def capture_video(cap, is_session_active, use_posenet=True):
#     if not is_session_active:
#         print("Error: Session is not active.")
#         return  # Don't proceed if the session is not active

#     if cap is None or not cap.isOpened():
#         print("Error: Camera is not initialized or cannot be opened.")
#         return

#     while cap.isOpened() and is_session_active:
#         ret, frame = cap.read()

#         if not ret:
#             print("Error: Frame not received from the camera.")
#             break

#         # Resize the frame for display
#         resized_frame = cv2.resize(frame, (840, 680))

#         # Perform pose evaluation and get feedback
#         feedback = evaluate_pose(resized_frame, use_posenet=use_posenet)

#         # Display the feedback on the frame
#         cv2.putText(resized_frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#         # Encode the frame as JPEG
#         success, buffer = cv2.imencode('.jpg', resized_frame)
#         if not success:
#             print("Error: Frame encoding failed.")
#             break

#         # Convert the buffer to bytes
#         frame_bytes = buffer.tobytes()

#         # Yield the frame in the required format for streaming
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

#     # Ensure the camera is released when done
#     if cap is not None:
#         cap.release()
#         print("Camera released successfully.")

import cv2
import numpy as np
from .real_time_pose_eval import evaluate_pose

def draw_grid(frame):
    height, width, _ = frame.shape
    grid_color = (255, 255, 255)  # White color for the grid
    grid_spacing = 50  # Adjust grid spacing as needed

    # Draw horizontal lines
    for y in range(0, height, grid_spacing):
        cv2.line(frame, (0, y), (width, y), grid_color, 1)

    # Draw vertical lines
    for x in range(0, width, grid_spacing):
        cv2.line(frame, (x, 0), (x, height), grid_color, 1)

    return frame

def draw_keypoints(frame, keypoints):
    for keypoint in keypoints:
        if isinstance(keypoint, np.ndarray) and keypoint.shape[0] >= 3:
            # Use .item() to get the scalar value if keypoint[2] is an array
            confidence = keypoint[2].item() if isinstance(keypoint[2], np.ndarray) else keypoint[2]

            if confidence > 0:  # Confidence score
                x = int(keypoint[0] * frame.shape[1])  # Scale x to frame width
                y = int(keypoint[1] * frame.shape[0])  # Scale y to frame height
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Draw a circle for the keypoint

    return frame


def capture_video(cap, is_session_active, use_posenet=True):
    if not is_session_active:
        print("Error: Session is not active.")
        return  # Don't proceed if the session is not active

    if cap is None or not cap.isOpened():
        print("Error: Camera is not initialized or cannot be opened.")
        return

    while cap.isOpened() and is_session_active:
        ret, frame = cap.read()

        if not ret:
            print("Error: Frame not received from the camera.")
            break

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (840, 680))

        # Perform pose evaluation and get feedback
        feedback, keypoints = evaluate_pose(resized_frame, use_posenet=use_posenet)

        # Draw grid on the frame
        frame_with_grid = draw_grid(resized_frame)

        # Draw keypoints on the frame
        frame_with_keypoints = draw_keypoints(frame_with_grid, keypoints)

        # Display the feedback on the frame
        cv2.putText(frame_with_keypoints, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Encode the frame as JPEG
        success, buffer = cv2.imencode('.jpg', frame_with_keypoints)
        if not success:
            print("Error: Frame encoding failed.")
            break

        # Convert the buffer to bytes
        frame_bytes = buffer.tobytes()

        # Yield the frame in the required format for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Ensure the camera is released when done
    if cap is not None:
        cap.release()
        print("Camera released successfully.")
