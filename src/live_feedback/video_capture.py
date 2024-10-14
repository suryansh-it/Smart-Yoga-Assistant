# Video capture setup with OpenCV for live input

"""
    Capture live video from the webcam and perform real-time pose evaluation.
    
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    """
import cv2
from .real_time_pose_eval import evaluate_pose

is_session_active = False
cap = None  # Declare capture variable globally

def start_video_capture(use_posenet=True):
    global is_session_active, cap
    is_session_active = True
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        is_session_active = False
        return

    while is_session_active:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (640, 480))

        # Perform pose evaluation and get feedback
        feedback = evaluate_pose(resized_frame, use_posenet=use_posenet)

        # Yield frame with feedback
        _, jpeg = cv2.imencode('.jpg', resized_frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    cap.release()

def stop_video_capture():
    global is_session_active
    is_session_active = False


# Video Capture as a Generator: The start_video_capture function now acts as a generator, 
# yielding video frames continuously until the session is marked as inactive.

# Global Variables: The global variable cap is used to maintain the state of the video capture
# , which can be accessed by both start_video_capture and stop_video_capture functions.

